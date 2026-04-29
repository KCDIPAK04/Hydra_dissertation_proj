from django.urls import path
from .views import main_dashboard,save_token

app_name = "dashboard"

urlpatterns = [
    path('', main_dashboard, name='home'),

    path('save-token/', save_token, name='save_token'),
]