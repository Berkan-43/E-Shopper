# Generated by Django 4.0.6 on 2022-11-15 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_product_subcategory_remove_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
