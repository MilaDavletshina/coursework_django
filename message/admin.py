from django.contrib import admin
from message.models import Client, Sms, Mail, Send


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
    list_display = ('first_dispatch', 'end_sending', 'status')
    search_fields = ('status',)


@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = ('data', 'sending_status', 'answer')
    search_fields = ('sending_status',)
    search_filter = ('sending_status',)