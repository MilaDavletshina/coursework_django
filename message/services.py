from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from config.settings import EMAIL_HOST_USER

from config.settings import CACHE_ENABLED
from message.models import Client, Mail, Send
from django.core.cache import cache
from django.utils import timezone


def run_mail(request, pk):
    """Функция запуск рассылки по требованию"""
    mailing = get_object_or_404(Mail, id=pk)
    for client in mailing.client.all():
        try:
            mailing.status = Mail.STATUS_LAUNCHED
            send_mail(
                topic=mailing.sms.topic,
                message=mailing.sms.content,
                from_email=EMAIL_HOST_USER,
                client_list=[client.email],
                fail_silently=False,
            )
            Send.objects.create(
                date_attempt=timezone.now(),
                status=Send.STATUS_OK,
                server_response='Email отправлен',
                mailing=mailing,
            )
        except Exception as e:
            print(f"Ошибка при отправке письма для {client.email}: {str(e)}")
            Send.objects.create(
                date_attempt=timezone.now(),
                status=Send.STATUS_NOK,
                server_response=str(e),
                mailing=mailing,
            )
    if mailing.end_sending and mailing.end_sending <= timezone.now():
        # Если время рассылки закончилось, обновляем статус на "завершено"
        mailing.status = Mail.STATUS_COMPETED
    mailing.save()
    return redirect('mailing:mail_list')


def get_clients_from_cash():
    """Получает данные из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Client.objects.all()

    key = "client_list"
    clients = cache.get(key)

    if clients is not None:
        return clients

    clients = Client.objects.all()
    cache.set(key, clients)

    return clients
