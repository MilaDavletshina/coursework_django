from django.contrib import admin
from message.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment')
    search_fields = ('name',)
    search_filter = ('name',)
