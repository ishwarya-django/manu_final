# Generated by Django 4.1.5 on 2023-01-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manu', '0004_remove_manufacturing_total_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_quantity', models.IntegerField()),
                ('quantity_price', models.IntegerField()),
                ('total_sell_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='total_amount',
            new_name='total_manufactured_amount',
        ),
    ]