from rest_framework import serializers

from . import models


class BudgetItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BudgetItemCategory
        fields = ("id", "name", "type")
