from django.contrib import admin
from home.models import *
# Register your models here.

admin.site.register(Setting)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'create_att',
        'note',
        'status',
    )
    readonly_fields = ["name", "email", "subject", "message", "create_att"]
    fieldsets = (
        ("MESAJLAR", {
            "fields": ("name", "email", "subject", "message", "create_att")
        }),
    )
    list_filter = (
        'subject',
        'status',
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return False

@admin.register(Faq)
class FaQAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'status',
        'create_att',
        'ordernumber',
    )
    list_filter = (
        'status',
    )