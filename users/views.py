import secrets

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    """Переход после регистрации на страницу пользователя"""
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет! Для подтверждения почты перейдите по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

    # def generate_new_password(request):
    #     new_password = get_new_password()
    #     send_mail(
    #         subject='Вы сменили пароль',
    #         message=f'Ваш новый пароль: {new_password}',
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[request.user.email]
    #     )
    #     request.user.set_password(new_password)
    #     request.user.save()
    #
    #     return redirect(reverse('users:login'))


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
