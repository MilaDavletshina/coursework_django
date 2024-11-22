
from django.urls import path
from django.views.decorators.cache import cache_page

from message.apps import MessageConfig
from message.services import run_mail
from message.views import (
    ClientListView,
    ClientDetailView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    SmsListView,
    SmsDetailView,
    SmsCreateView,
    SmsUpdateView,
    SmsDeleteView,
    MailListView,
    MailDetailView,
    MailCreateView,
    MailUpdateView,
    MailDeleteView,
    MainView,
    Contacts,
    Message, SendListView, SendCreateView,
)


app_name = MessageConfig.name

urlpatterns = [
    # path('', base, name='base.html'),
    path("", MainView.as_view(), name="main"),
    path("contacts/", Contacts.as_view(), name="contacts"),
    path("message/", Message.as_view(), name="message"),

    path("client/", cache_page(60)(ClientListView.as_view()), name="client_list"),
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client/create/", ClientCreateView.as_view(), name="client_create"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
    path("client/<int:pk>/run_mail/", run_mail, name="run_mail"),

    path("sms/list/", SmsListView.as_view(), name="sms_list"),
    path("sms/<int:pk>/", SmsDetailView.as_view(), name="sms_detail"),
    path("sms/create/", SmsCreateView.as_view(), name="sms_create"),
    path("sms/<int:pk>/update/", SmsUpdateView.as_view(), name="sms_update"),
    path("sms/<int:pk>/delete/", SmsDeleteView.as_view(), name="sms_delete"),

    path("mail/list/", MailListView.as_view(), name="mail_list"),
    path("mail/<int:pk>/", MailDetailView.as_view(), name="mail_detail"),
    path("mail/create/", MailCreateView.as_view(), name="mail_create"),
    path("mail/<int:pk>/update/", MailUpdateView.as_view(), name="mail_update"),
    path("mail/<int:pk>/delete/", MailDeleteView.as_view(), name="mail_delete"),
    path("mail/<int:pk>/run_mail/", run_mail, name="run_mail"),

    path("send/", SendListView.as_view(), name="send_list"),
    path("send/create/", SendCreateView.as_view(), name="send_create"),
]
