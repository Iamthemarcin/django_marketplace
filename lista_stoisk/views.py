from django.shortcuts import render
from stoisko.models import Stoisko
from stoisko.models import Produkt

def lista_stoisk(request):

    stoiska_zywnosc = Stoisko.objects.filter(czy_aktywne = True).filter(rodzaj_stoiska = 2)
    stoiska_ciuchy = Stoisko.objects.filter(czy_aktywne = True).filter(rodzaj_stoiska = 3)
    produkty = Produkt.objects.all()
    


    context = {
        'stoiska_zywnosc' : stoiska_zywnosc,
        'stoiska_ciuchy' : stoiska_ciuchy
    }
    
    
    
    return(render(request, 'lista_stoisk.html', context))

# Create your views here.
