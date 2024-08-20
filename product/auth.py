from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from customers.forms import LoginForm,RegisterForm
from customers.templates.customers import auth


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email,password=password)
            if user:
                login(request, user)
                return redirect('customer_list')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request,'product/registrat/login.html',{'form':form})


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            login(request, user)
            return redirect('customer_list')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = RegisterForm()

    return render(request, 'product/auth/register.html',{'form':form})

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('customer_list')