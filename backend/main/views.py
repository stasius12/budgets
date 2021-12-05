from rest_framework import viewsets

from .models import BudgetItemCategory, BudgetItem, Budget
from .serializers import (
    BudgetItemCategorySerializer,
    BudgetItemSerializer,
    BudgetSerializer,
)


class BudgetItemCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = BudgetItemCategory.objects.all()
    serializer_class = BudgetItemCategorySerializer


class BudgetItemModelViewSet(viewsets.ModelViewSet):
    queryset = BudgetItem.objects.all()
    serializer_class = BudgetItemSerializer


class BudgetModelViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
