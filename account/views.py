from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Account
from .forms import RegisterForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            acc=form.save()
            Account.objects.create(user=acc)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully registered")
            return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'account/register.html', {'form':form})
    return render(request, 'account/register.html', {'form':form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Error in logging in")
            return redirect('login')
    else:
        return render(request, 'account/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Succesfully logged out")
    return redirect('home')