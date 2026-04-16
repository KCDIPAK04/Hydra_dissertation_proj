from django.contrib import admin
from django.urls import path
from .views import login_view,signup_view, user_dashboard

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/',signup_view ,name='signup'),

    path('dashboard/',user_dashboard ,name='dashboard'),
]
