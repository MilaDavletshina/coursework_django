# Generated by Django 5.1.1 on 2024-10-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='введите e-mail', max_length=254, unique=True, verbose_name='e-mail')),
                ('name', models.CharField(help_text='укажите ФИО', max_length=100, verbose_name='ФИО')),
                ('comment', models.TextField(blank=True, help_text='оставьте комментарий', null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Получатель',
                'verbose_name_plural': 'Получатели',
                'ordering': ['name'],
            },
        ),
    ]
