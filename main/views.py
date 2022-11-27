from django.shortcuts import render, get_object_or_404, redirect


def home(request):


    return(render(request, 'home.html'))

# Create your views here.

def rejestracja(request):

    return(render(request, 'rejestracja.html'))