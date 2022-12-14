from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

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
    pass
