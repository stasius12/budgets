from rest_framework import routers

from .views import (
    BudgetItemCategoryModelViewSet,
    BudgetItemModelViewSet,
    BudgetModelViewSet,
)

router = routers.DefaultRouter()
router.register(
    "budgets/categories", BudgetItemCategoryModelViewSet, basename="budgets-categories"
)
router.register("budgets/items", BudgetItemModelViewSet, basename="budgets-items")
router.register("budgets/budgets", BudgetModelViewSet, basename="budgets")

urlpatterns = router.urls
