from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Uzytkownik, SprzedawcaProfile, Sprzedawca









class NewSellerForm(UserCreationForm):


	class Meta:
		model = Sprzedawca
		fields = ("username", "email", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.fields["username"].widget.attrs.update({
			'required' : 'true',
			'name':'username',
			'type':'text',
			'class':'form-control',
			'placeholder':'Nazwa użytkownika',
			'maxlength':'20',
			'minlength':'6'
		})
		self.fields["email"].widget.attrs.update({
			'required' : 'true',
			'name':'email',
			'type':'e-mail',
			'class':'form-control',
			'placeholder':'Adres e-mail',
		})
		self.fields["password1"].widget.attrs.update({
			'required' : 'true',
			'name':'password1',
			'type':'password',
			'class':'form-control',
			'placeholder':'Hasło',
			'maxlength':'20',
			'minlength':'6'
		})
		self.fields["password2"].widget.attrs.update({
			'required' : 'true',
			'name':'password2',
			'type':'password',
			'class':'form-control',
			'placeholder':'Powtórz hasło',
			'maxlength':'20',
			'minlength':'6'
		})

class NewSellerInfoForm(forms.ModelForm):

	class Meta:
		model = SprzedawcaProfile
		fields = ("imie", "nazwisko")
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.fields["imie"].widget.attrs.update({
			'required' : 'true',
			'name':'imie',
			'type':'text',
			'class':'form-control',
			'placeholder':'Wpisz swoje imie',
			'maxlength':'34',
			'minlength':'2'
		})
		self.fields["nazwisko"].widget.attrs.update({
			'required' : 'true',
			'name':'nazwisko',
			'type':'text',
			'class':'form-control',
			'placeholder':'Wpisz swoje nazwisko',
			'maxlength':'34',
			'minlength':'2'
		})

class NewNormalUserForm(NewSellerForm):
		class Meta:
			model = Uzytkownik	
			fields = ("username", "email", "password1", "password2")
		
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)