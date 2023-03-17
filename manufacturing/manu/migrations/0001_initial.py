# Generated by Django 4.1.5 on 2023-01-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charges_name', models.CharField(blank=True, max_length=20, null=True)),
                ('charges_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
