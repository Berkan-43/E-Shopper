# Generated by Django 4.0.6 on 2022-12-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
