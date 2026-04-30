from django.urls import path
from .views import login_view, signup_view,user_profile

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),

    path('user_profile',user_profile, name='user_profile'),
]