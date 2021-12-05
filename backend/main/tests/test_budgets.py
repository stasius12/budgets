import pytest
from rest_framework import status

from main.enums import BudgetItemType
from main.models import BudgetItemCategory, BudgetItem, Budget


def test_creating_item_category(api_client, db):
    response = api_client.post(
        "/budgets/categories/", {"name": "Shopping", "type": BudgetItemType.EXPENSE}
    )
    assert response.status_code == status.HTTP_201_CREATED

    created_category = BudgetItemCategory.objects.get()
    assert created_category.name == "Shopping"
    assert created_category.type == BudgetItemType.EXPENSE


def test_create_category_with_existing_names_return_400(
    api_client, budget_item_category_factory, db
):
    budget_item_category_factory(name="Shopping")

    response = api_client.post(
        "/budgets/categories/", {"name": "Shopping", "type": BudgetItemType.EXPENSE}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    assert BudgetItemCategory.objects.count() == 1


def test_create_item(api_client, item_payload):
    response = api_client.post(
        "/budgets/items/",
        item_payload,
    )
    assert response.status_code == status.HTTP_201_CREATED

    created_item = BudgetItem.objects.get()
    for field, value in item_payload.items():
        item_value = getattr(created_item, field)
        if field in ["category", "budget"]:
            assert item_value.id == value
        else:
            assert item_value == value


@pytest.mark.parametrize(
    "missing_param, res_status",
    [
        # required params
        ("name", status.HTTP_400_BAD_REQUEST),
        ("value", status.HTTP_400_BAD_REQUEST),
        ("budget", status.HTTP_400_BAD_REQUEST),
        # optional params
        ("type", status.HTTP_201_CREATED),
        ("currency", status.HTTP_201_CREATED),
        ("category", status.HTTP_201_CREATED),
        ("description", status.HTTP_201_CREATED),
    ],
)
def test_create_item_required_params(
    api_client, item_payload, missing_param, res_status
):
    item_payload.pop(missing_param)

    response = api_client.post(
        "/budgets/items/",
        item_payload,
    )
    assert response.status_code == res_status


def test_create_item_default_values_applied(api_client, minimal_item_payload, db):
    response = api_client.post(
        "/budgets/items/",
        minimal_item_payload,
    )
    assert response.status_code == status.HTTP_201_CREATED

    created_item = BudgetItem.objects.get()
    assert created_item.type == BudgetItemType.EXPENSE
    assert created_item.currency == BudgetItem.Currency.USD
    assert created_item.category is None
    assert created_item.description == ""


def test_create_budget(api_client, user):
    response = api_client.post(
        "/budgets/budgets/",
        {
            "name": "Monthly budget",
            "user": user.id,
            "description": "Some description",
        },
    )

    assert response.status_code == status.HTTP_201_CREATED

    created_budget = Budget.objects.get()
    assert created_budget.name == "Monthly budget"
    assert created_budget.user == user
    assert created_budget.description == "Some description"
