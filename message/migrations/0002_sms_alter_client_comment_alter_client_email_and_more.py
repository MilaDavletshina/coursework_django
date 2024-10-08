# Generated by Django 5.1.1 on 2024-10-08 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(help_text='Укажите тему письма', max_length=100, verbose_name='Тема')),
                ('content', models.TextField(blank=True, help_text='Добавьте содержание', null=True, verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.TextField(blank=True, help_text='Добавьте комментарий', null=True, verbose_name='комментарий'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(help_text='Введите e-mail', max_length=254, unique=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(help_text='Укажите ФИО', max_length=100, verbose_name='ФИО'),
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_dispatch', models.DateTimeField(auto_now_add=True)),
                ('end_sending', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('completed', 'строка: Завершена'), ('created', 'строка: Создана'), ('launched', 'строка: Запущена')], default='completed', max_length=10, verbose_name='Строка')),
                ('client', models.ManyToManyField(to='message.client')),
                ('sms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mail', to='message.sms')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ['status'],
            },
        ),
    ]
