# Generated by Django 5.1 on 2024-08-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(blank=True, choices=[('owner', '烟花'), ('admin', '小幫手'), ('member', '小羊')], default='member', max_length=10),
        ),
    ]
