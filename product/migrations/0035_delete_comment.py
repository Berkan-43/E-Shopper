# Generated by Django 4.0.6 on 2022-11-25 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_remove_comment_user_comment_comment_write'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]