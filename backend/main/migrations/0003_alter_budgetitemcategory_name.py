# Generated by Django 3.2.9 on 2021-12-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_budget_budgetitem_budgetitemcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetitemcategory',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
