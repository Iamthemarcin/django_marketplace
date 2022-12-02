from django.shortcuts import render
from .models import Stoisko
from main.models import Sprzedawca 
from komentarze.forms import CommentForm
from komentarze.models import Komentarz
from django.contrib import messages

# Create your views here.





def stoisko(request, id):

    moje_stoisko = Stoisko.objects.get(id = id)
    sprzedawca = Sprzedawca.objects.get(username = moje_stoisko.sprzedawca)
    context = {}

    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
    

        if not request.user.is_authenticated:
            messages.error(request, 'Username OR password is incorrect')
        
        if comment_form.is_valid():

            new_comment = Komentarz()

            new_comment.tekst = comment_form.cleaned_data['tekst']

            new_comment.stoisko = moje_stoisko
            new_comment.kreator = request.user
            new_comment.save()
            



    comment_form = CommentForm()
    context = {'comment_form': comment_form}


    komentarze = moje_stoisko.komentarze.all()
    context.update({
        'moje_stoisko':moje_stoisko,
        'sprzedawca': sprzedawca,
        'komentarze': komentarze
    })


    return(render(request, 'stoisko.html', context))

# Create your views here.
