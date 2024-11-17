from django.utils import timezone
from django.core.mail import send_mail
from django.core.management import BaseCommand

from config.settings import EMAIL_HOST_USER
from message.models import Send, Mail


class Command(BaseCommand):
    help = "Отправка почтовых отправлений получателям"

    def handle(self, *args, **kwargs):
        mailings = Mail.objects.filter(
            status__in=[Mail.STATUS_CREATED, Mail.STATUS_LAUNCHED]
        )
        for mailing in mailings:
            for recipient in mailing.recipients.all():
                try:
                    send_mail(
                        mailing.sms.topic,
                        mailing.sms.content,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[recipient.email],
                        fail_silently=False,
                    )
                    Send.objects.create(
                        data=timezone.now(),
                        sending_status=Send.STATUS_OK,
                        answer="Email отправлен",
                        status=mailing,
                    )
                    print(
                        f"Сообщение {mailing.sms.topic} успешно отправлено на  {recipient.email}"
                    )
                except Exception as e:
                    Send.objects.create(
                        data=timezone.now(),
                        sending_status=Send.STATUS_NOK,
                        answer=str(e),
                        status=mailing,
                    )
                    print(str(e))
            mailing.save()
