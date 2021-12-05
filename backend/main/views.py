from rest_framework import viewsets

from .models import BudgetItemCategory
from .serializers import BudgetItemCategorySerializer


class BudgetItemCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = BudgetItemCategory.objects.all()
    serializer_class = BudgetItemCategorySerializer
