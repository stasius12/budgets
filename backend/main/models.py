from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .enums import BudgetItemType


class User(AbstractUser):
    pass


class BudgetItemCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.IntegerField(
        choices=BudgetItemType.choices, default=BudgetItemType.EXPENSE
    )

    class Meta:
        verbose_name_plural = _("Budget item categories")

    def __str__(self):
        return self.name


class Budget(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(
        blank=True, help_text=_("Description and purpose for creating this budget.")
    )

    def __str__(self):
        return f"{self.name} <{self.user}>"


class BudgetItem(models.Model):
    class Currency(models.TextChoices):
        USD = "USD", _("U.S. Dollar (USD)")
        EUR = "EUR", _("European Euro (EUR)")
        GBP = "GBP", _("British Pound (GBP)")
        CHF = "CHF", _("Swiss Franc (CHF)")
        PLN = "PLN", _("Polish Złoty (PLN)")

    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    type = models.IntegerField(
        choices=BudgetItemType.choices, default=BudgetItemType.EXPENSE
    )
    currency = models.CharField(
        max_length=3, choices=Currency.choices, default=Currency.USD
    )
    category = models.ForeignKey(
        BudgetItemCategory, blank=True, null=True, on_delete=models.SET_NULL
    )
    description = models.TextField(
        blank=True,
        help_text=_("Additional information about the record in the budget."),
    )

    def __str__(self):
        return f"{self.name} - {self.value} {self.currency} <{self.category.name}>"
