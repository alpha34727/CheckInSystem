from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .form import PromiseForm
from .models import LeaveApply

# Create your views here.

class Homepage(LoginRequiredMixin, ListView):
    model = LeaveApply
    login_url = reverse_lazy('login')

    def get_context_data(self):
        content = super().get_context_data()
        content['name'] = User.objects.get(id=1)
        
        return content

    template_name = 'homepage.html'
    context_object_name = 'ctx'

class Apply(LoginRequiredMixin, CreateView):
    model = LeaveApply

    login_url = reverse_lazy('login')
    template_name = 'apply.html'
    form_class = PromiseForm

    success_url = reverse_lazy('home')

    def form_valid(self, form):
        now_form = form.save(commit=False)
        now_form.MemberID = self.request.user.id
        now_form.save()
        return super().form_valid(form)

class CheckIn(LoginRequiredMixin, CreateView):
    model = LeaveApply()
