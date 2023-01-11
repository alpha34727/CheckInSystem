from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Member

# Create your views here.

class Homepage(LoginRequiredMixin, ListView):
    model = Member
    login_url = reverse_lazy('login')

    template_name = 'homepage.html'
    context_object_name = 'member'

