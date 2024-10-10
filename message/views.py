from django.shortcuts import render
from django.urls import reverse_lazy

from message.models import Client, Sms, Mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def base(request):
    return render(request, "base.html")


class ClientListView(ListView):
    model = Client

# app_name/<model_name>_<action> т.е будет message/client_list.html


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ("email", "name", "comment")
    success_url = reverse_lazy("message:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    fields = ("email", "name", "comment")
    success_url = reverse_lazy("message:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("message:client_list")


class SmsListView(ListView):
    model = Sms


class SmsDetailView(DetailView):
    model = Sms


class SmsCreateView(CreateView):
    model = Sms
    fields = ("topic", "content")
    success_url = reverse_lazy("message:sms_list")


class SmsUpdateView(UpdateView):
    model = Sms
    fields = ("topic", "content")
    success_url = reverse_lazy("message:sms_list")


class SmsDeleteView(DeleteView):
    model = Sms
    success_url = reverse_lazy("message:sms_list")


class MailListView(ListView):
    model = Mail


class MailDetailView(DetailView):
    model = Mail


class MailCreateView(CreateView):
    model = Mail
    fields = ("status", "sms", "client")
    success_url = reverse_lazy("message:mail_list")


class MailUpdateView(UpdateView):
    model = Mail
    fields = ("status", "sms", "client")
    success_url = reverse_lazy("message:mail_list")


class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy("message:mail_list")