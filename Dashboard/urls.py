from django.urls import path, include
from .views import Homepage, Apply, CheckIn, ListAttendant, register

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('auth/', include('django.contrib.auth.urls'), name='auth'),
    path('auth/register/', register, name='register'),
    path('apply/', Apply.as_view(), name='apply'),
    path('check/<int:pk>/', CheckIn.as_view(), name='check'),
    path('attendant/', ListAttendant.as_view(), name='attendant'),
]
