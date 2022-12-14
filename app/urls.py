from django.urls import path
from .views import HomePage

urlpatterns = [
    path('home/', HomePage, name='home-page')
]
