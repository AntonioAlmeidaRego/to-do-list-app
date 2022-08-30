from django.contrib import admin

# Register your models here.
from store.models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ('created_at',)
    ordering = ['name']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Store, StoreAdmin)

admin.site.site_header = "Sistema de Lojas - Painel Admin"
