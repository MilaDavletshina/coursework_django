from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy


from message.forms import (
    ClientForm,
    SmsForm,
    MailForm,
    ClientModeratorForm,
    SmsModeratorForm,
    MailModeratorForm, SendForm,
)
from message.models import Client, Sms, Mail, Send
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from message.services import get_clients_from_cash, get_send_from_cash


def base(request):
    """Основной шаблон"""
    return render(request, "base.html")


class Contacts(TemplateView):
    """Шаблон контакты"""

    template_name = "message/contacts.html"

    def contacts(request):
        if request.method == "POST":
            name = request.POST.get("name")  # получаем имя
            message = request.POST.get("message")  # получаем сообщение
            return HttpResponse(f"Спасибо, {name}! {message} Сообщение получено.")
        return render(request, "message/contacts.html")


class Message(TemplateView):
    """Страница ответа на отправленное сообщение"""

    template_name = "message/message.html"


class MainView(TemplateView):
    """Главная страница"""

    template_name = "message/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mail_count"] = len(Mail.objects.all())
        context["active_count"] = len(Mail.objects.filter(status="Запущен"))
        context["unique_email"] = len(Client.objects.all())
        return context


class ClientListView(ListView):
    """Получатели рассылок - просмотр"""

    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_queryset(self):
        return get_clients_from_cash()
# app_name/<model_name>_<action> т.е будет message/client_list.html


class ClientDetailView(DetailView, LoginRequiredMixin):
    """Получатель рассылки"""

    model = Client
    form_class = ClientForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


class ClientCreateView(CreateView, LoginRequiredMixin):
    """Получатель рассылки - создание"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("message:client_list")

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView, LoginRequiredMixin):
    """Получатель рассылки - обновление"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("message:client_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("message.can_unblocking_client") and user.has_perm(
            "message.can_disabling_mailings"
        ):
            return ClientModeratorForm
        return ClientForm


class ClientDeleteView(DeleteView):
    """Получатель рассылки - удаление"""

    model = Client
    success_url = reverse_lazy("message:client_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


class SmsListView(ListView):
    """Сообщения - просмотр"""

    model = Sms


class SmsDetailView(DetailView, LoginRequiredMixin):
    """Просмотр выбранного сообщения"""

    model = Sms

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


class SmsCreateView(CreateView, LoginRequiredMixin):
    """Сообщения - создание"""

    model = Sms
    form_class = SmsForm
    success_url = reverse_lazy("message:sms_list")

    def form_valid(self, form):
        sms = form.save()
        user = self.request.user
        sms.owner = user
        sms.save()

        return super().form_valid(form)


class SmsUpdateView(UpdateView, LoginRequiredMixin):
    """Сообщения - обновление"""

    model = Sms
    form_class = SmsForm
    success_url = reverse_lazy("message:sms_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("message.can_unblocking_sms") and user.has_perm(
            "message.can_disabling_mailings"
        ):
            return SmsModeratorForm
        return SmsForm


class SmsDeleteView(DeleteView):
    """Сообщения - удаление"""

    model = Sms
    success_url = reverse_lazy("message:sms_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


class MailListView(ListView):
    """Рассылка - просмотр"""

    model = Mail


class MailDetailView(DetailView, LoginRequiredMixin):
    """Просмотр выбранной рассылки"""

    model = Mail

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


class MailCreateView(CreateView, LoginRequiredMixin):
    """Рассылка - создание"""

    model = Mail
    form_class = MailForm
    success_url = reverse_lazy("message:mail_list")

    def form_valid(self, form):
        mail = form.save()
        user = self.request.user
        mail.owner = user
        mail.save()


class MailUpdateView(UpdateView, LoginRequiredMixin):
    """Рассылка - обновление"""

    model = Mail
    form_class = MailForm
    success_url = reverse_lazy("message:mail_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("message.can_unblocking_mailing") and user.has_perm(
            "message.can_disabling_mailings"
        ):
            return MailModeratorForm
        return MailForm


class MailDeleteView(DeleteView):
    """Рассылка - удаление"""

    model = Mail
    success_url = reverse_lazy("message:mail_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


class SendListView(ListView, LoginRequiredMixin):
    model = Send

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_queryset(self):
        return get_send_from_cash()


class SendCreateView(LoginRequiredMixin, CreateView):
    model = Send
    form_class = SendForm

    def form_valid(self, form):
        send = form.save()
        user = self.request.user
        send.owner = user
        send.save()