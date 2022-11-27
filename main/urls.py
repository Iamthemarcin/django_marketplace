from django.urls import re_path
from django.urls import path
from . import views


urlpatterns = [

    re_path(r'', views.home, name = 'home'),
    re_path(r'rejestracja/', views.rejestracja, name = 'rejestracja')
    #logowanie i rejestracja 
    
]