from rest_framework import routers

from .views import BudgetItemCategoryModelViewSet

router = routers.DefaultRouter()
router.register(
    "budgets/categories", BudgetItemCategoryModelViewSet, basename="budgets-categories"
)

urlpatterns = router.urls
