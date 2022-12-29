from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    adress = models.CharField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, null=True, max_length=15)
    email = models.CharField(blank=True, null=True, max_length=50)
    smtpserver = models.CharField(blank=True, null=True, max_length=20)
    smtpemail = models.CharField(blank=True, null=True, max_length=20)
    smtppassword = models.CharField(blank=True, null=True, max_length=10)
    smtpport = models.CharField(max_length=5, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, null=True, max_length=50)
    instagram = models.CharField(blank=True, null=True, max_length=50)
    aboutus = RichTextField()
    contact = RichTextField(blank=True)
    references = RichTextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Ayarlar'
        verbose_name_plural = 'Ayarlar'
        verbose_name = 'Ayar'

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('Read', 'Okundu'),
        ('Closed', 'Kapalı'),
    )
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(max_length=100, blank=True)
    create_att = models.DateTimeField(auto_now_add=True)
    update_att = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'İletişim'
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.name

    
class Faq(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=150)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_att = models.DateTimeField(auto_now_add=True)
    update_att = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'S.S.S'
        verbose_name = 'S.S.S'
        verbose_name_plural = 'S.S.S'

    def __str__(self):
        return self.question