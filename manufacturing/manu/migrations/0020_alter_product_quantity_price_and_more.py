# Generated by Django 4.1.5 on 2023-01-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manu', '0019_product_quantity_price_product_sell_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]