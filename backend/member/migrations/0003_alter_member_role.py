# Generated by Django 5.1 on 2024-09-01 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_member_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(blank=True, choices=[('烟花', 'Owner'), ('小幫手', 'Admin'), ('小羊', 'Member')], default='小羊', max_length=10),
        ),
    ]