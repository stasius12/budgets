from django.db import models
from django.utils.translation import gettext_lazy as _


class BudgetItemType(models.IntegerChoices):
    INCOME = 0, _("Income")
    EXPENSE = 1, _("Expense")
