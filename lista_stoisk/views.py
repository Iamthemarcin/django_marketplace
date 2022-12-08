from django.shortcuts import render
from stoisko.models import Stoisko
from stoisko.models import Produkt



def wyszukaj(request):

    if request.method == 'POST':
        zapytanie = request.POST.get('zapytanie')
        stoiska = Stoisko.objects.filter(produkt__nazwa_produktu__icontains=zapytanie)
        stoiska_zywnosc = stoiska.filter(czy_aktywne = True).filter(rodzaj_stoiska = 2).filter(sprzedawca != null).order_by("id")
        stoiska_ciuchy = stoiska.filter(czy_aktywne = True).filter(rodzaj_stoiska = 3).filter(sprzedawca != null).order_by("id")
        
        context = {
                'stoiska_zywnosc' : stoiska_zywnosc,
                'stoiska_ciuchy' : stoiska_ciuchy
        }

        return (render(request, 'lista_stoisk.html', context))
    else:
        return lista_stoisk(request)


def lista_stoisk(request):

    stoiska_zywnosc = Stoisko.objects.filter(czy_aktywne = True).filter(rodzaj_stoiska = 2).order_by("id")
    stoiska_ciuchy = Stoisko.objects.filter(czy_aktywne = True).filter(rodzaj_stoiska = 3).order_by("id")
    produkty = Produkt.objects.all()
    
    context = {
        'stoiska_zywnosc' : stoiska_zywnosc,
        'stoiska_ciuchy' : stoiska_ciuchy
    }
        
    return(render(request, 'lista_stoisk.html', context))

# Create your views here.
