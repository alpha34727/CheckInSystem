from django.urls import path, include
from .views import Homepage

urlpatterns = [
    path('', Homepage.as_view()),
    path('auth/', include('django.contrib.auth.urls'), name='auth'),
]
