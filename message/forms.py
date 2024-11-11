from django import forms
from django.forms import ModelForm, BooleanField, DateTimeInput

from .models import Client, Sms, Mail, Send


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild.name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class SmsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Sms
        fields = '__all__'


class MailForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'

        widgets = {
            'start_date': DateTimeInput(attrs={'placeholder': 'ДД.ММ.ГГГГ ЧЧ:ММ:СС', 'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'placeholder': 'ДД.ММ.ГГГГ ЧЧ:ММ:СС', 'type': 'datetime-local'}),
        }


class SendForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Send
        fields = '__all__'

