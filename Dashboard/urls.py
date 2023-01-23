from django.urls import path, include
from .views import Homepage, Apply, CheckIn, register, PasswordChange, CheckAttendant

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('auth/', include('django.contrib.auth.urls'), name='auth'),
    path('auth/register/', register, name='register'),
    path('auth/password/', PasswordChange.as_view(), name='password'),
    path('apply/', Apply.as_view(), name='apply'),
    path('check/<int:pk>/', CheckIn.as_view(), name='check'),
    path('attcheck/<int:year>/<int:month>/', CheckAttendant.as_view(), name='attcheck'),
]
