from django.shortcuts import render
from .models import Stoisko
# Create your views here.

def stoisko(request, id):




    moje_stoisko = Stoisko.objects.get(id = id)
    context = {
        'moje_stoisko':moje_stoisko
    }

    return(render(request, 'stoisko.html', context))

# Create your views here.
