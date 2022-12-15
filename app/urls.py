from django.urls import path
from .views import HomePage, RegisterPage, LoginPage

urlpatterns = [
    path('home/', HomePage, name='home-page'),
    path('register/', RegisterPage, name='register-page'),
    path('login/', LoginPage, name='login-page'),
]
