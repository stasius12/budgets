from decimal import Decimal
from typing import Dict, Any

import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import (
    BudgetItemCategoryFactory,
    BudgetItemFactory,
    BudgetFactory,
    UserFactory,
)
from main.enums import BudgetItemType
from main.models import BudgetItem, User


register(BudgetItemCategoryFactory)
register(BudgetItemFactory)
register(BudgetFactory)
register(UserFactory)


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def user(user_factory, db) -> User:
    return user_factory()


@pytest.fixture
def minimal_item_payload(budget_factory, user) -> Dict[str, Any]:
    monthly = budget_factory(name="Monthly", user=user)

    return {
        "name": "new jeans",
        "value": Decimal("19.95"),
        "budget": monthly.id,
    }


@pytest.fixture
def item_payload(budget_item_category_factory, minimal_item_payload) -> Dict[str, Any]:
    shopping = budget_item_category_factory(name="Shopping")

    return {
        **minimal_item_payload,
        "type": BudgetItemType.EXPENSE,
        "currency": BudgetItem.Currency.EUR,
        "category": shopping.id,
        "description": "But my new extra important pair of jeans",
    }
