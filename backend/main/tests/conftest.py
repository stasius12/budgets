import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import BudgetItemCategoryFactory

register(BudgetItemCategoryFactory)


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()
