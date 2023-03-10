# Generated by Django 4.0.6 on 2022-11-27 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0039_alter_comment_product_alter_comment_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_alter_shopcart_options_alter_shopcart_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(editable=False, max_length=5)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, choices=[('New', 'Yeni'), ('Accepted', 'Kabul Edildi'), ('Preaparing', 'Hazırlanıyor'), ('OnShihipping', 'Kargoda'), ('Complated', 'Tamamlanmış'), ('Canceled', 'İptal Edildi')], max_length=20)),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('Accepted', 'Kabul Edildi'), ('Preaparing', 'Hazırlanıyor'), ('OnShihipping', 'Kargoda'), ('Complated', 'Tamamlanmış'), ('Canceled', 'İptal Edildi')], default='New', max_length=12)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('create_att', models.DateTimeField(auto_now_add=True)),
                ('update_att', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sipariş',
                'verbose_name_plural': 'Siparişler',
                'db_table': 'Siparişler',
            },
        ),
        migrations.CreateModel(
            name='OderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('Accepted', 'Kabul Edildi'), ('Canceled', 'İptal Edildi')], default='New', max_length=12)),
                ('create_att', models.DateTimeField(auto_now_add=True)),
                ('update_att', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
