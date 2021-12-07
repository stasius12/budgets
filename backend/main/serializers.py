from rest_framework import serializers

from . import models


class BudgetItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BudgetItemCategory
        fields = ("id", "name", "type")


class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BudgetItem
        fields = (
            "id",
            "name",
            "value",
            "budget",
            "type",
            "currency",
            "category",
            "description",
        )


class BudgetSerializer(serializers.ModelSerializer):
    budgetitem_set = BudgetItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Budget
        fields = (
            "id",
            "name",
            "user",
            "description",
            "budgetitem_set",
        )
