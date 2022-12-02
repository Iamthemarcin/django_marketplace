from django.contrib import admin
from .models import Komentarz

# Register your models here.
@admin.register(Komentarz)
class KomentarzAdmin(admin.ModelAdmin):
    list_display = ('kreator', 'tekst', 'stoisko', 'stworzono')

    search_fields = ('kreator', 'tekst')
