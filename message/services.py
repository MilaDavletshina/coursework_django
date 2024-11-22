from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from config.settings import EMAIL_HOST_USER

from config.settings import CACHE_ENABLED
from message.models import Client, Mail, Send
from django.core.cache import cache
from django.utils import timezone


def run_mail(request, pk):
    """Рассылка по требованию"""
    mailing = get_object_or_404(Mail, id=pk)
    for i in mailing.client.all():
        try:
            mailing.status = Mail.STATUS_LAUNCHED

            send_mail(
                topic=mailing.sms.topic,
                message=mailing.sms.content,
                from_email=EMAIL_HOST_USER,
                client_list=[i.email],
                fail_silently=False,
            )
            Send.objects.create(
                data=timezone.now(),
                sending_status=Send.STATUS_OK,
                answer="Email отправлен",
                status=mailing,
            )

        except Exception as e:
            print(f"Ошибка при отправке письма для {i.email}: {str(e)}")
            Send.objects.create(
                data=timezone.now(),
                sending_status=Send.STATUS_NOK,
                answer=str(e),
                status=mailing,
            )
    if mailing.end_sending and mailing.end_sending <= timezone.now():
        # Если время рассылки закончилось, обновляем статус на "завершен"
        mailing.status = Mail.STATUS_COMPETED
    mailing.save()
    return redirect("mailing:mail_list")


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

