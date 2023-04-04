from django.urls import path
from base import views

urlpatterns = [
    path('home/', views.home_runner, name='home'),
    path('profile/', views.profile_runner, name='profile'),
]
