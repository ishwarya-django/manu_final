# Generated by Django 4.1.4 on 2023-01-31 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manu', '0030_sellproduct_is_active_sellproduct_status_sell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufactured_quantity',
            field=models.CharField(max_length=60),
        ),
    ]
