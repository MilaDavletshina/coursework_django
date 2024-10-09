from django.urls import path
from message.apps import MessageConfig
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
    SmsDeleteView
)


app_name = MessageConfig.name

urlpatterns = [
    # path('', base, name='base.html'),
    path("", ClientListView.as_view(), name="client_list"),
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client/create/", ClientCreateView.as_view(), name="client_create"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
    path("sms/list/", SmsListView.as_view(), name="sms_list"),
    path("sms/<int:pk>/", SmsDetailView.as_view(), name="sms_detail"),
    path("sms/create/", SmsCreateView.as_view(), name="sms_create"),
    path("sms/<int:pk>/update/", SmsUpdateView.as_view(), name="sms_update"),
    path("sms/<int:pk>/delete/", SmsDeleteView.as_view(), name="sms_delete")
]
