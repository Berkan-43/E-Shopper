# Generated by Django 4.0.6 on 2022-11-17 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_rename_urun_comment_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
