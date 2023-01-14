from django.shortcuts import render
from django.views.generic import ListView, CreateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .form import PromiseForm
from .models import LeaveApply, Member, Attendant
from django.utils import timezone
import pytz

# Create your views here.

class Homepage(LoginRequiredMixin, ListView):
    model = LeaveApply
    login_url = reverse_lazy('login')

    ordering = ['-id']

    def get_context_data(self):
        content = super().get_context_data()
        content['check'] = Member.objects.get(MemberID=self.request.user.id).CheckIn
        content['hadcheck'] = Attendant.objects.filter(MemberID=self.request.user.id)
        content['start'] = Member.objects.get(MemberID=self.request.user.id).StartTime
        content['Now'] = timezone.localtime()
        
        return content

    template_name = 'homepage.html'
    context_object_name = 'ctx'

class Apply(LoginRequiredMixin, CreateView):
    model = LeaveApply

    login_url = reverse_lazy('login')
    template_name = 'apply.html'
    form_class = PromiseForm

    success_url = reverse_lazy('home')

    def get_context_data(self):
        content = super().get_context_data()
        content['check'] = Member.objects.get(MemberID=self.request.user.id).CheckIn
        
        return content

    def form_valid(self, form):
        now_form = form.save(commit=False)
        now_form.MemberID = self.request.user.id
        now_form.save()
        return super().form_valid(form)

class CheckIn(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        member = Member.objects.get(MemberID=self.request.user.id)
        member.StartTime = timezone.localtime()
        member.CheckIn = not member.CheckIn
        member.save()

        if not member.CheckIn:
            Attendant.objects.create(MemberID=member.MemberID, Start=member.StartTime, End=timezone.localtime())

        return reverse_lazy('home')

class ListAttendant(LoginRequiredMixin, ListView):
    model=Attendant
    login_url = reverse_lazy('login')

    def get_context_data(self):
        month = timezone.localtime().month
        if month == 1:
            month_str = "一"
        elif month == 2:
            month_str = "二"
        elif month == 3:
            month_str = "三"
        elif month == 4:
            month_str = "四"
        elif month == 5:
            month_str = "五"
        elif month == 6:
            month_str = "六"
        elif month == 7:
            month_str = "七"
        elif month == 8:
            month_str = "八"
        elif month == 9:
            month_str = "九"
        elif month == 10:
            month_str = "十"
        elif month == 11:
            month_str = "十一"
        elif month == 12:
            month_str = "十二"
        else:
            month_str = "123"

        content = super().get_context_data()
        content['month'] = month_str
        content['Now'] = timezone.localtime()
        content['day_loop'] = range(1, timezone.localtime().day + 1)
        content['check'] = Member.objects.get(MemberID=self.request.user.id).CheckIn
        
        
        return content

    template_name = 'list_attendant.html'
    context_object_name = 'ctx'
