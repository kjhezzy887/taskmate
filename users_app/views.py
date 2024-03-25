from django.shortcuts import render, redirect
from users_app.forms import CustomRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            messages.success(request, ("New User Account Created. Login to get started")) 
            return redirect('login')
    else:
        register_form = CustomRegistrationForm()
    return render(request, 'register.html', {'register_form': register_form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            messages.success(request, ('Invalid Login Details!'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('home')