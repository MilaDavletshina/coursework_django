from django.forms import ModelForm

from message.models import Client, Sms, Mail, Send


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ("can_blocking_client", "owner")


class SmsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Sms
        fields = "__all__"
        exclude = ("can_blocking_sms", "owner")


class MailForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mail
        fields = "__all__"
        exclude = ("set_is_active", "owner")


class SendForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Send
        fields = "__all__"


class ClientModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ["can_blocking_client",]


class SmsModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ["can_blocking_sms",]


class MailModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ["set_is_active",]


class SendModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Send
        fields = "__all__"
