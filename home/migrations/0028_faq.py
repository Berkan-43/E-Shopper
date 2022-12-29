# Generated by Django 4.0.6 on 2022-12-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_att', models.DateTimeField(auto_now_add=True)),
                ('update_att', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'S.S.S',
                'verbose_name_plural': 'S.S.S',
                'db_table': 'S.S.S',
            },
        ),
    ]