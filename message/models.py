from django.db import models


class Client(models.Model):
    """Получатель рассылки"""
    email = models.EmailField(unique=True, verbose_name='e-mail', help_text='введите e-mail')
    name = models.CharField(max_length=100, verbose_name='ФИО', help_text='укажите ФИО')
    comment = models.TextField(null=True, blank=True, verbose_name='комментарий', help_text='оставьте комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
        ordering = ['name',]


# class Sms(models.Model):
#     """Сообщение"""
