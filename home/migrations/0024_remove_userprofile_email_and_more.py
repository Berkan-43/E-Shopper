# Generated by Django 4.0.6 on 2022-11-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_userprofile_email_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]
