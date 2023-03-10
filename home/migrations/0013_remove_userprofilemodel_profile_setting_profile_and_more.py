# Generated by Django 4.0.6 on 2022-11-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_userprofilemodel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='profile',
        ),
        migrations.AddField(
            model_name='setting',
            name='profile',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='images',
            field=models.ImageField(blank=True, upload_to='image/profile/'),
        ),
    ]
