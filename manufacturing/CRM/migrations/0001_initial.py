# Generated by Django 4.1.4 on 2023-01-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
                ('phone_number', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('doorno', models.CharField(max_length=50, null=True)),
                ('address_line1', models.CharField(max_length=50, null=True)),
                ('address_line2', models.CharField(max_length=50, null=True)),
                ('place', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
