from django.urls import re_path
from . import views


urlpatterns = [

    re_path(r'', views.lista_stoisk, name = 'lista_stoisk'),


]