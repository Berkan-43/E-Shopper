# Generated by Django 4.0.6 on 2022-11-26 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_setting_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='profile',
        ),
    ]
