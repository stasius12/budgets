import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "main.User"


class BudgetItemCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "main.BudgetItemCategory"


class BudgetItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "main.BudgetItem"


class BudgetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "main.Budget"
