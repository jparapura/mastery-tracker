from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request, 'index.html', {})

def Register(request):
    pass

def Login(request):
    pass
