from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def HomePage(request):
    return render(request, 'index.html', {})

def RegisterPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        # new_user.first_name = fname

        new_user.save()
        return redirect('home-page')


    return render(request, 'register.html', {})

def LoginPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('pass')
        
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('User does not exist.')

    return render(request, 'login.html', {})


def LogoutPage(request):
    logout(request)
    return redirect('login-page')
