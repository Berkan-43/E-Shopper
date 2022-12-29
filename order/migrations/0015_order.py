# Generated by Django 4.0.6 on 2022-12-09 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0043_alter_comment_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0014_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('Preparing', 'Hazırlanıyor'), ('cargo', 'Kargoda'), ('Approved', 'Onaylandı'), ('It_is_cancelled', 'İptal Edildi')], default='New', max_length=15)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('cargo', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]