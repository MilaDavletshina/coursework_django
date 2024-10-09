from django.shortcuts import render
from django.urls import reverse_lazy

from message.models import Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def base(request):
    return render(request, "base.html")


class ClientListView(ListView):
    model = Client

# app_name/<model_name>_<action> т.е будет message/client_list.html


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ("email", "name", "comment")
    success_url = reverse_lazy("message:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    fields = ("email", "name", "comment")
    success_url = reverse_lazy("message:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("message:client_list")