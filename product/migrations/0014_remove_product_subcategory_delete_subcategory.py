# Generated by Django 4.0.6 on 2022-11-14 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_category'),
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