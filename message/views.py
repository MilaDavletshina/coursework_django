from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from message.models import Client, Sms, Mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


def base(request):
    return render(request, "base.html")


class Contacts(TemplateView):
    template_name = "message/contacts.html"

    def contacts(request):
        if request.method == 'POST':
            name = request.POST.get('name')  # получаем имя
            message = request.POST.get('message')  # получаем сообщение

            return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
        return render(request, 'message/contacts.html')


class Message(TemplateView):
    template_name = "message/message.html"


class MainView(TemplateView):
    template_name = 'message/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mail_count'] = len(Mail.objects.all())
        context['active_count'] = len(Mail.objects.filter(status='Запущен'))
        context['unique_email'] = len(Client.objects.all())
        return context


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

    def mail_send(request):
        if request.method == 'POST':
            name = request.POST.get('client')  # получаем имя
            message = request.POST.get('sms')  # получаем сообщение

            return HttpResponse(f"Спасибо, {client}!  Рассылка создана.")
        return render(request, 'message/mail_list.html')


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