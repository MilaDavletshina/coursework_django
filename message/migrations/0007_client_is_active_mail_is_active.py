# Generated by Django 4.2.2 on 2024-11-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0006_alter_client_options_alter_mail_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="активность"),
        ),
        migrations.AddField(
            model_name="mail",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="активна"),
        ),
    ]
