from django.db.models import BooleanField
from django.forms import ModelForm

from message.models import Client, Sms, Mail


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class SmsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Sms
        fields = "__all__"


class MailForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mail
        fields = "__all__"