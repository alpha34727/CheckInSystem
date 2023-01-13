from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .form import PromiseForm
from .models import Member, Attendant

# Create your views here.

class Homepage(ListView):
    model = Member
    login_url = reverse_lazy('login')

    def get_context_data(self):
        content = super().get_context_data()
        content['name'] = User.objects.get(id=1)
        
        return content

    template_name = 'homepage.html'
    context_object_name = 'member'

class Apply(LoginRequiredMixin, CreateView):
    model = Attendant

    template_name = 'apply.html'
    form_class = PromiseForm

    success_url = reverse_lazy('home')
