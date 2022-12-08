from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/edytowanie/', views.edytowanie, name = "edytowanie"),
    path('<int:id>/<int:ocena>/', views.ocena, name = "ocena"),
    path('<int:id>/polubienie/', views.polubiono, name = "polubiono"),
    path('<int:id>/', views.stoisko, name = 'stoisko'),


]