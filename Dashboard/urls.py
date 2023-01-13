from django.urls import path, include
from .views import Homepage, Apply

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('auth/', include('django.contrib.auth.urls'), name='auth'),
    path('apply/', Apply.as_view()),
]
