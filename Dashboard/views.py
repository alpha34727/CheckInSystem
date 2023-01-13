from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .form import PromiseForm
from .models import Member, Attendant

# Create your views here.

class Homepage(LoginRequiredMixin, ListView):
    model = Member
    login_url = reverse_lazy('login')

    template_name = 'homepage.html'
    context_object_name = 'member'

class Apply(LoginRequiredMixin, CreateView):
    model = Attendant

    template_name = 'apply.html'
    form_class = PromiseForm

    success_url = reverse_lazy('home')
