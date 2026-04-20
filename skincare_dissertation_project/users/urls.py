from django.urls import path
from .views import login_view, signup_view, complete_profile

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('complete-profile/', complete_profile, name='complete_profile'),
]