# Generated by Django 2.2 on 2021-10-28 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20211027_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartlist',
            old_name='cart_id',
            new_name='c_id',
        ),
    ]
