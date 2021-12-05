import factory


class BudgetItemCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "main.BudgetItemCategory"
