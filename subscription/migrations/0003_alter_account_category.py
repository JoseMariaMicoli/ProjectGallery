# Generated by Django 4.2.4 on 2023-08-19 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_category_selfie'),
        ('subscription', '0002_rename_category_account_category_account_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]
