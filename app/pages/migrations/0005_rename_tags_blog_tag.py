# Generated by Django 3.2.23 on 2024-01-18 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20240117_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tags',
            new_name='tag',
        ),
    ]
