from django.contrib import admin
from .models import Member, LeaveApply, Attendant

# Register your models here.

admin.site.register(Member)
admin.site.register(Attendant)
admin.site.register(LeaveApply)