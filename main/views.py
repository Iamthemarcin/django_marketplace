from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewNormalUserForm, NewSellerForm, NewSellerInfoForm
from .models import Sprzedawca, SprzedawcaProfile
def home(request):


    return(render(request, 'home.html'))

# Create your views here.






def rejestracja(request):

    if request.method == "POST":
        seller_form = NewSellerForm(request.POST)
        seller_info_form = NewSellerInfoForm(request.POST)
        user_form = NewNormalUserForm(request.POST)
        if seller_form.is_valid() and seller_info_form.is_valid():
            
            seller_form.save()

            username = seller_form.cleaned_data['username']
            password = seller_form.cleaned_data['password1']
            sprzedawca = Sprzedawca.objects.get(username = username)
            sprzedawca_info = SprzedawcaProfile.objects.get(pk=sprzedawca.id)
            sprzedawca_info.imie = seller_info_form.cleaned_data['imie']
            sprzedawca_info.nazwisko = seller_info_form.cleaned_data['nazwisko']
            sprzedawca_info.save()

            user = authenticate(username = username, password = password)    
               
            login(request, user)
            return(render(request, 'home.html'))
        
        elif user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']

            user = authenticate(username = username, password = password)
            
            login(request, user)
            messages.success(request, "Pomyślnie zarejestrowano")
            return(render(request, 'home.html'))
        
        else:
            context = {
                'errors' : user_form.errors,
                'form': user_form
            }
            print(user_form.errors)
            return(render(request, 'rejestracja.html', context))

    else:
        seller_form = NewSellerForm()
        seller_info_form = NewSellerInfoForm()
        user_form = NewNormalUserForm()
        context = {
            'seller_form': seller_form,
            'seller_info_form': seller_info_form,
            'user_form': user_form,

        }

        return(render(request, 'rejestracja.html', context))
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


def logowanie(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return(render(request, 'home.html'))
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Nie ma takiego użytkownika")
            return(render(request, 'logowanie.html'))
    
    return(render(request, 'logowanie.html'))

def wylogowywanie(request):
    logout(request)
    return(render(request,'home.html'))