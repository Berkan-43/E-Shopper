# Generated by Django 4.0.6 on 2022-11-24 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_customusermodel_usermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]