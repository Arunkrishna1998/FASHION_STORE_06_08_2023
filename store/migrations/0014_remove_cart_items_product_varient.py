# Generated by Django 4.2.3 on 2023-07-18 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_cart_items_product_varient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_items',
            name='product_varient',
        ),
    ]
