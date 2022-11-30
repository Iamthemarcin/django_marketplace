from django.contrib import admin
from .models import Sprzedawca, Uzytkownik, SprzedawcaProfile
# Register your models here.


admin.site.register(Sprzedawca)
admin.site.register(Uzytkownik)
admin.site.register(SprzedawcaProfile)

