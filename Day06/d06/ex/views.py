from django.shortcuts import render, redirect
import random
from django.conf import settings
from .forms import SingUpForm, SingInForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def Home(request):
    response = ""
    if 'userCookies' in request.COOKIES:
        username = request.COOKIES['userCookies']
        response = render(request, 'home.html', {'username': username})
    else:
        username = random.choice(settings.USER_NAME)
        response = render(request, 'home.html', {'username': username})
        response.set_cookie('userCookies', username, max_age=settings.COOKIES_AGE)

    return response

def SingUp(request):
    form = SingUpForm()
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            retry_password = form.cleaned_data.get('retry_password')
            if password != retry_password:
                print('Password not match')
                messages.error(request, 'Password not match')
                return redirect('SingUp')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('SingUp')
            elif not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('profile')
    return render(request, 'SingUp.html',{'form':form})

def SingIn(request):
    form = SingInForm()
    if request.method == 'POST':
        form = SingInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                print('Username or password is incorrect')
                messages.error(request, 'Username or password is incorrect')
                return redirect('SingIn')
            else:
                login(request, user)
                messages.success(request, 'Login successfully')
                print('Login successfully')
                return redirect('profile')
    return render(request, 'SingIn.html',{'form':form})


def SingOut(request):
    logout(request)
    messages.success(request, 'Logout successfully')

    return render(request, 'SingOut.html')

def Profile(request):
    username = request.user.username
    print(username)
    return render(request, 'profile.html', {'username': username})
