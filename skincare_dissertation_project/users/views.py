from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from datetime import date
from dashboard.models import DailyLogin

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            DailyLogin.objects.get_or_create(
                user=user,
                date=date.today()
            )
            return redirect('dashboard:home')
    return render(request, 'registration/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('complete_profile')
        else:
            messages.error(request, 'Signup error')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_profile(request):
    return render(request, 'userProfile/user_profile.html')