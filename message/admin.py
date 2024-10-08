from django.contrib import admin
from message.models import Client, Sms, Mail


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment')
    search_fields = ('name',)
    search_filter = ('name',)


@admin.register(Sms)
class SmsAdmin(admin.ModelAdmin):
    list_display = ('topic', 'content')
    search_fields = ('topic',)


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('first_dispatch', 'end_sending', 'status', 'sms__topic')
    search_fields = ('status',)