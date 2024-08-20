# customers/auth.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, RegisterForm

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('customer_list')
    return render(request, 'customers/auth/login.html', {'form': form})

def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    return render(request, 'customers/auth/register.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('login_page')
