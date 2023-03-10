from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    STATUS = [
        ('True', 'Evet'),
        ('False', 'Hayır'), 
    ]
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='category')
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(blank=True, max_length=10, choices=STATUS)
    slug = AutoSlugField(populate_from='title', unique=True)
    create_att = models.DateTimeField(auto_now_add=True)
    update_att = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Kategoriler'
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    keywords = models.CharField(max_length=255)
    description = models.CharField(blank=True, null=True,max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='image/')
    price = models.FloatField()
    discounted_price= models.FloatField(blank=True, null=True)
    amount = models.IntegerField()
    detail = RichTextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Ürünler'
        verbose_name_plural = 'Ürünler'
        verbose_name = 'Ürün'

    def __str__(self):
        return self.title

class Images(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='image/')

    class Meta:
        db_table = 'Ürün-Resimleri'
        verbose_name_plural = 'Ürün-Resimleri'
        verbose_name = 'Ürün-Resmi'

    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = [
        ('New', 'Bekliyor'),
        ('True', 'Onaylandı'),
        ('False', 'Reddedildi'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='yorum')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='yazan')
    subject = models.CharField(max_length=50)
    comment = models.TextField(max_length=200)
    rate = models.IntegerField(blank=True, null=True)
    status = models.CharField(blank=True, choices=STATUS, max_length=10, default='New')
    ip = models.CharField(max_length=20, blank=True)
    create_att = models.DateTimeField(auto_now_add=True)
    update_att = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Yorumlar'
        verbose_name_plural = 'Yorumlar'
        verbose_name = 'Yorum'

    def __str__(self):
        return self.subject


    