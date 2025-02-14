# Generated by Django 5.1.1 on 2024-10-08 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0002_sms_alter_client_comment_alter_client_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mail",
            name="client",
            field=models.ManyToManyField(
                to="message.client", verbose_name="Получатель"
            ),
        ),
        migrations.AlterField(
            model_name="mail",
            name="end_sending",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата окончания отправки"
            ),
        ),
        migrations.AlterField(
            model_name="mail",
            name="first_dispatch",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата первой отправки"
            ),
        ),
        migrations.AlterField(
            model_name="mail",
            name="sms",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mail",
                to="message.sms",
                verbose_name="Сообщение",
            ),
        ),
        migrations.AlterField(
            model_name="mail",
            name="status",
            field=models.CharField(
                choices=[
                    ("completed", "статус: Завершен"),
                    ("created", "статус: Создан"),
                    ("launched", "статус: Запущен"),
                ],
                default="completed",
                max_length=10,
                verbose_name="Статус рассылки",
            ),
        ),
        migrations.CreateModel(
            name="Send",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата попытки рассылки"
                    ),
                ),
                (
                    "sending_status",
                    models.CharField(
                        choices=[
                            ("ok", "статус: Успешно"),
                            ("not ok", "статус: Не успешно"),
                        ],
                        default="ok",
                        max_length=10,
                        verbose_name="Статус попытки рассылки",
                    ),
                ),
                (
                    "answer",
                    models.TextField(
                        blank=True, null=True, verbose_name="Ответ почтового сервера"
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="send",
                        to="message.mail",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
        ),
    ]
