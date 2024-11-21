from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.forms import ModelForm
from django.urls import reverse_lazy

from message.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя"""
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserForm(StyleFormMixin, UserChangeForm):
    """Форма данных пользователя"""
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "phone",
            "avatar",
            "country",
        )


class UserUpdateForm(StyleFormMixin, ModelForm):
    """Форма обновления данных пользователя"""
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "phone",
            "avatar",
            "country",
        )
        success_url = reverse_lazy("users:user_list")


class UserForgotPasswordForm(PasswordResetForm):
    """Форма запроса на восстановление пароля"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "autocomplete": "off"}
            )


class UserSetNewPasswordForm(SetPasswordForm):
    """Форма изменения пароля пользователя после подтверждения"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "autocomplete": "off"}
            )
