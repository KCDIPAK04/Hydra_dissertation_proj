from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Error in signup process')

    return render(request, 'registration/login.html')


def signup_view(request):
    if request.method == 'POST':
        # importing custom form from custom user creation form
        form = CustomUserCreationForm(request.POST)

        # Form for user Input and checking it's validity
        if form.is_valid():
            user = form.save()
            # Explicitly specify the backend when logging in
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('home')
        else:
            messages.error(request, 'Error in signup process')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def user_dashboard(request):
    return render(request, 'users/userDashboard.html')
