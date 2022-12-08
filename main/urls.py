from django.urls import re_path
from django.urls import path
from . import views
from lista_stoisk import views as l_views


urlpatterns = [

    path('', views.home, name = 'home'),

    #logowanie i rejestracja 
    path('rejestracja/', views.rejestracja, name = 'rejestracja'),
    path('logowanie/', views.logowanie, name = 'logowanie'),
    path('wylogowywanie/', views.wylogowywanie, name = 'wylogowywanie'),
    path('wyszukano/', l_views.wyszukaj, name = 'wyszukaj')
]
