from django.db import models


class Client(models.Model):
    """Получатель рассылки"""
    email = models.EmailField(unique=True, verbose_name='e-mail', help_text='Введите e-mail') # Email (строка, уникальное)
    name = models.CharField(max_length=100, verbose_name='ФИО', help_text='Укажите ФИО') # Ф.И.О. (строка)
    comment = models.TextField(null=True, blank=True, verbose_name='комментарий', help_text='Добавьте комментарий') # Комментарий (текст)

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

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mail(models.Model):
    """Рассылка"""
    STATUS_COMPETED = 'completed'
    STATUS_CREATED = 'created'
    STATUS_LAUNCHED = 'launched'

    STATUS_CHOICES = [
        (STATUS_COMPETED, 'строка: Завершена'),
        (STATUS_CREATED, 'строка: Создана'),
        (STATUS_LAUNCHED, 'строка: Запущена'),
    ]
    first_dispatch = models.DateTimeField(auto_now_add=True, verbose_name='Дата первой отправки') # Дата и время первой отправки
    end_sending = models.DateTimeField(auto_now_add=True, verbose_name='Дата окончания отправки') # Дата и время окончания отправки
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_COMPETED, verbose_name='Статус строки') # Статус (строка: 'Завершена', 'Создана', 'Запущена')
    sms = models.ForeignKey(Sms, on_delete=models.CASCADE, related_name='mail', verbose_name='Сообщение') # Сообщение (внешний ключ на модель «Сообщение»)
    client = models.ManyToManyField(Client, verbose_name='Получатель') # Получатели («многие ко многим», связь с моделью «Получатель»)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status',]
