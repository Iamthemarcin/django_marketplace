from .models import Komentarz
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Komentarz
        fields = ('tekst', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tekst"].widget.attrs.update({
			'required' : 'true',
			'name':'tekst',
			'type':'text',
			'class':'form-control mr-3',
			'placeholder':'Dodaj komentarz',
			'maxlength':'360',
			'minlength':'1'
		})