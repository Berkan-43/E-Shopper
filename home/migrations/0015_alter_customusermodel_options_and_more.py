# Generated by Django 4.0.6 on 2022-11-25 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_setting_profile_customusermodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customusermodel',
            options={'verbose_name': 'CustomUser', 'verbose_name_plural': 'CustomUser'},
        ),
        migrations.AlterModelTable(
            name='customusermodel',
            table='CustomUser',
        ),
    ]