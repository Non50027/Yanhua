# Generated by Django 5.1 on 2024-08-16 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_user_order_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2024, 8, 16)),
        ),
    ]