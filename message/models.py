from django.db import models

from users.models import User


class Client(models.Model):
    """Получатель рассылки"""
    email = models.EmailField(unique=True, verbose_name='e-mail', help_text='Введите e-mail') # Email (строка, уникальное)
    name = models.CharField(max_length=100, verbose_name='ФИО', help_text='Укажите ФИО') # Ф.И.О. (строка)
    comment = models.TextField(null=True, blank=True, verbose_name='комментарий', help_text='Добавьте комментарий') # Комментарий (текст)
    is_active = models.BooleanField(default=True, verbose_name='активность')
    owner = models.ForeignKey(User, verbose_name='Получатель', help_text='укажите получателя рассылки', blank=True,
                              null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
        ordering = ['name',]


class Sms(models.Model):
    """Сообщение"""
    topic = models.CharField(max_length=100, verbose_name='Тема', help_text='Укажите тему письма') # Тема письма (строка)
    content = models.TextField(null=True, blank=True, verbose_name='Содержание', help_text='Добавьте содержание') # Тело письма (текст)
    owner = models.ForeignKey(User, verbose_name='Владелец сообщения', help_text='укажите Владельца сообщения', blank=True,
                              null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mail(models.Model):
    """Рассылка"""
    STATUS_COMPETED = 'Завершен'
    STATUS_CREATED = 'Создан'
    STATUS_LAUNCHED = 'Запущен'

    STATUS_CHOICES = [
        (STATUS_COMPETED, 'статус: Завершен'),
        (STATUS_CREATED, 'статус: Создан'),
        (STATUS_LAUNCHED, 'статус: Запущен'),
    ]

    first_dispatch = models.DateTimeField(auto_now_add=True, verbose_name='Дата первой отправки') # Дата и время первой отправки
    end_sending = models.DateTimeField(auto_now_add=True, verbose_name='Дата окончания отправки') # Дата и время окончания отправки
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_LAUNCHED, verbose_name='Статус рассылки') # Статус
    sms = models.ForeignKey(Sms, on_delete=models.CASCADE, related_name='mail', verbose_name='Сообщение') # Сообщение (внешний ключ на модель «Сообщение»)
    client = models.ManyToManyField(Client, verbose_name='Получатель') # Получатели («многие ко многим», связь с моделью «Получатель»)
    is_active = models.BooleanField(default=True, verbose_name='активна')
    owner = models.ForeignKey(User, verbose_name='Владелец рассылки', help_text='укажите Владельца рассылки', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status',]
        permissions = [
            ('set_is_active', 'set is active')
        ]


class Send(models.Model):
    """Попытка рассылки"""
    STATUS_OK = 'Успешно'
    STATUS_NOK = 'Не успешно'

    STATUS_CHOICES = [
        (STATUS_OK, 'статус: Успешно'),
        (STATUS_NOK, 'статус: Не успешно'),
    ]

    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата попытки рассылки') # Дата и время попытки
    sending_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_OK, verbose_name='Статус попытки рассылки')
    answer = models.TextField(null=True, blank=True, verbose_name='Ответ почтового сервера')
    status = models.ForeignKey(Mail, on_delete=models.CASCADE, related_name='send', verbose_name='Рассылка')  # внешний ключ на модель «Рассылка»

    def __str__(self):
        return self.sending_status

    class Meta:
        verbose_name = 'Управление рассылкой'
        verbose_name_plural = 'Управление рассылками'
        ordering = ['sending_status',]


# class Log(models.Model):
#     """Логирование попытки рассылки"""
#     mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='Рассылка')
#     last_time_mail = models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')
#     status = models.CharField(max_length=50, verbose_name='Статус попытки')
#     response = models.TextField(verbose_name='Ответ сервера', null=True, blank=True)
#
#     def __str__(self):
#         return (f'Дата и время последней попытки: {self.last_time_mail}.'
#                 f' Статус попытки:{self.status}')
#
#     class Meta:
#         verbose_name = 'Лог'
#         verbose_name_plural = 'Логи'