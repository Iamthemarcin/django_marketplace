from django.shortcuts import render
from .models import Stoisko, Ocena
from main.models import Sprzedawca 
from komentarze.forms import CommentForm
from komentarze.models import Komentarz, Polubienie
from django.contrib import messages
from django.http import JsonResponse
import json



# Create your views here.

def edytowanie(request, id):
    
    moje_stoisko = Stoisko.objects.get(id = id)

    if request.method == "POST":
        print('hello')

    context = {
        'moje_stoisko': moje_stoisko
    }
    
    return render(request,'edycja_stoiska.html', context)


def polubiono(request, id):

    if request.method == "POST":
        data = json.loads(request.body)
        komentarz_id = data['komentarz_id']
        komentarz = Komentarz.objects.get(id = komentarz_id)
        uzytkownik = request.user
        polubienie = Polubienie.objects.filter(uzytkownik = uzytkownik, komentarz = komentarz)
        if polubienie:
            polubienie.delete()
            ilosc_polubien = komentarz.ilosc_polubien
            return JsonResponse({'ilosc_polubien': ilosc_polubien})
        else:                
            polubienie = Polubienie()
            polubienie.komentarz = komentarz 
            polubienie.uzytkownik = uzytkownik      
            polubienie.save()
            ilosc_polubien = komentarz.ilosc_polubien
            return JsonResponse({'ilosc_polubien': ilosc_polubien})


def ocena(request, id, ocena):

    moje_stoisko = Stoisko.objects.get(id=id)
    Ocena.objects.filter(stoisko=moje_stoisko, kreator=request.user).delete()
    ocena = Ocena(kreator = request.user, stoisko = moje_stoisko, ocena = ocena)
    ocena.save()
    return stoisko(request, id)

def stoisko(request, id):

    moje_stoisko = Stoisko.objects.get(id = id)
    sprzedawca = Sprzedawca.objects.get(username = moje_stoisko.sprzedawca)
    if request.user.is_authenticated:    
        ocena = Ocena.objects.filter(stoisko=moje_stoisko, kreator=request.user).first()
        if ocena:
            moje_stoisko.ocena = ocena.ocena
    else:
        ocena = 0 
    
    context = {}

    
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)


        
        if comment_form.is_valid() and request.user.is_authenticated:

            new_comment = Komentarz()
            new_comment.tekst = comment_form.cleaned_data['tekst']
            new_comment.stoisko = moje_stoisko
            new_comment.kreator = request.user
            new_comment.save()
            
        else:
            return(render(request, 'logowanie.html'))
    comment_form = CommentForm()
    context = {'comment_form': comment_form}
    komentarze = moje_stoisko.komentarze.all().order_by("id")

    context.update({
        'moje_stoisko':moje_stoisko,
        'sprzedawca': sprzedawca,
        'ocena': ocena,
        'komentarze': komentarze
    })

    return(render(request, 'stoisko.html', context))

# Create your views here.
