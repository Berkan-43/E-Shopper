# Generated by Django 4.0.6 on 2022-11-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_setting_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
