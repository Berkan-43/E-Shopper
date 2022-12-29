from django.contrib import admin
from .models import *


# Register your models here.

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'create_att',
        'update_att',
    )
    search_fields = (
        'title',
        'status',
        'category__title',
    )
    list_filter = (
        'status',
        'category__title',
    )



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'discounted_price',
        'amount',
    ]
        
    
    list_filter = (
        'category',
        'status',
    )

    search_fields = (
        'title',
        'price',
        'status',
    )
    inlines = [ProductImagesInline]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'product',
        'image',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'comment',
        'status'
    )
    list_filter = (
        'status',
    )
