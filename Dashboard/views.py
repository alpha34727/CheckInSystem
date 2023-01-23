from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, RedirectView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .form import PromiseForm
from .models import LeaveApply, Member, Attendant
from django.utils import timezone
import calendar

# Create your views here.

class Homepage(LoginRequiredMixin, ListView):
    model = LeaveApply
    login_url = reverse_lazy('login')

    ordering = ['-id']

    def get_context_data(self):
        content = super().get_context_data()
        content['Now'] = timezone.localtime()
        content['check'] = Member.objects.get(MemberID=self.request.user.id).CheckIn
        content['hadcheck'] = Attendant.objects.filter(MemberID=self.request.user.id)
        content['start'] = Member.objects.get(MemberID=self.request.user.id).StartTime
        
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
        content['Now'] = timezone.localtime()
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

class CheckAttendant(LoginRequiredMixin, ListView):
    model = Attendant

    def get_context_data(self):
        month = self.kwargs['month']
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
            month_str = "一"

        content = super().get_context_data()
        content['Now'] = timezone.localtime()
        content['month'] = month_str
        if self.kwargs['year'] == timezone.localtime().year and self.kwargs['month'] == timezone.localtime().month:
            content['day_loop'] = range(1, timezone.localtime().day + 1)
        else:
            content['day_loop'] = range(1, calendar.monthrange(self.kwargs['year'], self.kwargs['month'])[1] + 1)
        content['check'] = Member.objects.get(MemberID=self.request.user.id).CheckIn
        content['Y'] = self.kwargs['year']
        if 1 <= self.kwargs['month'] and self.kwargs['month'] <= 12:
            content['M'] = self.kwargs['month']
        else:
            content['M'] = 1

        return content

    template_name = 'check_attendant.html'
    context_object_name = 'ctx'

def register(req):
    form = UserCreationForm(req.POST)
    if form.is_valid():
        form.save()
        Member.objects.create(MemberID=User.objects.last().id)

        return redirect(reverse_lazy('home'))
    else:
        return render(req, 'registration/register.html', {'form':form})

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    login_url = reverse_lazy('login')

    template_name = 'registration/password.html'

    def get_context_data(self):
        content = super().get_context_data()
        content['Now'] = timezone.localtime()
        return content
    
