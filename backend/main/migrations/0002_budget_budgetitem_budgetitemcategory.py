# Generated by Django 3.2.9 on 2021-12-04 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.IntegerField(choices=[(0, 'Income'), (1, 'Expense')], default=1)),
            ],
            options={
                'verbose_name_plural': 'Budget item categories',
            },
        ),
        migrations.CreateModel(
            name='BudgetItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.IntegerField(choices=[(0, 'Income'), (1, 'Expense')], default=1)),
                ('currency', models.CharField(choices=[('USD', 'U.S. Dollar (USD)'), ('EUR', 'European Euro (EUR)'), ('GBP', 'British Pound (GBP)'), ('CHF', 'Swiss Franc (CHF)'), ('PLN', 'Polish Złoty (PLN)')], default='USD', max_length=3)),
                ('description', models.TextField(blank=True, help_text='Additional information about the record in the budget.')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.budgetitemcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, help_text='Description and purpose for creating this budget.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
