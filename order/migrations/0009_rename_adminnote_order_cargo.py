# Generated by Django 4.0.6 on 2022-12-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adminnote',
            new_name='cargo',
        ),
    ]
