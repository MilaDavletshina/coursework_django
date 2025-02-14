# Generated by Django 4.2.2 on 2024-11-13 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("message", "0004_alter_send_options_alter_mail_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="укажите получателя рассылки",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Получатель",
            ),
        ),
        migrations.AddField(
            model_name="mail",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="укажите Владельца рассылки",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец рассылки",
            ),
        ),
        migrations.AddField(
            model_name="sms",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="укажите Владельца сообщения",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец сообщения",
            ),
        ),
    ]
