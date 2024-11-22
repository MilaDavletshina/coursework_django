from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER

from config.settings import CACHE_ENABLED
from message.models import Client, Send
from django.core.cache import cache
from django.utils import timezone


def to_run_mail(mail):
    """Отправка рассылки вручную через интерфейс"""
    clients = mail.client.all()
    for client in clients:
        try:
            answer = send_mail(
                mail.sms.topic,
                mail.sms.content,
                from_email=EMAIL_HOST_USER,
                recipient_list=[client.email],
                fail_silently=False,
            )
            sending_status = 'Успешно'

        except Exception as e:
            answer = str(e)
            sending_status = 'Не успешно'

        Send.objects.create(
            mail=mail,
            sending_status=sending_status,
            answer=answer
        )

    # Обновление статуса рассылки
    if sending_status == 'Успешно':
        mail.status = 'Запущен'
        mail.first_dispatch = timezone.now()
        mail.save()


def get_clients_from_cash():
    """Получает данные из кэша по получателям рассылки, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Client.objects.all()

    key = "client_list"
    clients = cache.get(key)

    if clients is not None:
        return clients

    clients = Client.objects.all()
    cache.set(key, clients)

    return clients


def get_send_from_cash():
    """Получает данные из кэша по попыткам рассылки, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Send.objects.all()

    key = "send_list"
    sends = cache.get(key)

    if sends is not None:
        return sends

    sends = Send.objects.all()
    cache.set(key, sends)

    return sends
