from rest_framework import status

from main.enums import BudgetItemType
from main.models import BudgetItemCategory


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
