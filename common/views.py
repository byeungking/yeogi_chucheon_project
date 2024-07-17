from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomLoginForm, CustomSignUpForm

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mainApp:main_home')
    else:
        form = CustomLoginForm()
    return render(request, 'common/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('mainApp:main_home')
    else:
        form = CustomSignUpForm()
    return render(request, 'common/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('mainApp:main_home')