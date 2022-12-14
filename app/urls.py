from django.urls import path
from .views import HomePage, RegisterPage

urlpatterns = [
    path('home/', HomePage, name='home-page'),
    path('register/', RegisterPage, name='register-page')
]
