from django.urls import path
from . import views


urlpatterns = [

    path('<int:id>/', views.stoisko, name = 'stoisko'),


]