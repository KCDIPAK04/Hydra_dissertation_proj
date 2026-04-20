from django.urls import path
from .views import main_dashboard

app_name = "dashboard"

urlpatterns = [
    path('', main_dashboard, name='home'),
]