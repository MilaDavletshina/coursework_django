from datetime import timezone

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from message.forms import ClientForm, SmsForm, MailForm
from message.models import Client, Sms, Mail, Send
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


def base(request):
    """Основной шаблон"""
    return render(request, "base.html")


class Contacts(TemplateView):
    """Шаблон контакты"""
    template_name = "message/contacts.html"

    def contacts(request):
        if request.method == 'POST':
            name = request.POST.get('name')  # получаем имя
            message = request.POST.get('message')  # получаем сообщение

            return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
        return render(request, 'message/contacts.html')


class Message(TemplateView):
    """Страница ответа на отправленное сообщение"""
    template_name = "message/message.html"


class MainView(TemplateView):
    """Главная страница"""
    template_name = 'message/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mail_count'] = len(Mail.objects.all())
        context['active_count'] = len(Mail.objects.filter(status='Запущен'))
        context['unique_email'] = len(Client.objects.all())
        return context


class ClientListView(ListView):
    """Получатели рассылок - просмотр"""
    model = Client

# app_name/<model_name>_<action> т.е будет message/client_list.html


class ClientDetailView(DetailView):
    """Получатель рассылки"""
    model = Client


class ClientCreateView(CreateView):
    """Получатель рассылки - создание"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("message:client_list")

    def form_valid(self, form):
        self.object = form.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    """Получатель рассылки - обновление"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("message:client_list")


class ClientDeleteView(DeleteView):
    """Получатель рассылки - удаление"""
    model = Client
    success_url = reverse_lazy("message:client_list")


class SmsListView(ListView):
    """Сообщения - просмотр"""
    model = Sms


class SmsDetailView(DetailView):
    """Просмотр выбранного сообщения"""
    model = Sms


class SmsCreateView(CreateView):
    """Сообщения - создание"""
    model = Sms
    form_class = SmsForm
    success_url = reverse_lazy("message:sms_list")


class SmsUpdateView(UpdateView):
    """Сообщения - обновление"""
    model = Sms
    form_class = SmsForm
    success_url = reverse_lazy("message:sms_list")


class SmsDeleteView(DeleteView):
    """Сообщения - удаление"""
    model = Sms
    success_url = reverse_lazy("message:sms_list")


class MailListView(ListView):
    """Рассылка - просмотр"""
    model = Mail


class MailDetailView(DetailView):
    """Просмотр выбранной рассылки"""
    model = Mail


class MailCreateView(CreateView):
    """Рассылка - создание"""
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy("message:mail_list")


class MailUpdateView(UpdateView):
    """Рассылка - обновление"""
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy("message:mail_list")


class MailDeleteView(DeleteView):
    """Рассылка - удаление"""
    model = Mail
    success_url = reverse_lazy("message:mail_list")


def send_mail(mail):
    """Функция отправки сообщений по требованию"""
    clients = mail.client.all()
    for client in clients:
        try:
            response = send_mail(
                mail.message.subject,
                mail.message.body,
                'from@example.com',
                [client.email],
            )
            status = 'Успешно'
        except Exception as e:
            response = str(e)
            status = 'Не успешно'

        Send.objects.create(
            mail=mail,
            status=status,
            answer=response
        )

    # Обновление статуса рассылки
    if status == 'Успешно':
        mail.status = 'Запущен'
        mail.first_dispatch = timezone.now()
        mail.save()
