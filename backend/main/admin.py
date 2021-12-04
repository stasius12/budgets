from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


admin.site.register(models.User, UserAdmin)


@admin.register(models.BudgetItemCategory)
class BudgetItemCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ("type",)


@admin.register(models.BudgetItem)
class BudgetItemAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "type", "currency", "category")
    list_filter = ("type", "category")


@admin.register(models.Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    list_filter = ("user",)
