# Generated by Django 5.0 on 2024-01-06 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_alter_item_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='for_user',
        ),
    ]