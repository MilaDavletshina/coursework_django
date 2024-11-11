from django.contrib.auth.views import LoginView
from django.urls import path
from message.apps import MessageConfig


app_name = MessageConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login')
]
