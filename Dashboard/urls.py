from django.urls import path, include
from .views import Homepage, Apply, CheckIn

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('auth/', include('django.contrib.auth.urls'), name='auth'),
    path('apply/', Apply.as_view(), name='apply'),
    path('checkin/', CheckIn.as_view(), name='checkin')
]
