from __future__ import unicode_literals
from django.db import models
from main.models import Sprzedawca
# Create your models here.

class Stoisko(models.Model):

    
    INNE = 1
    ŻYWNOŚĆ = 2
    CIUCHY = 3


    RODZAJE_STOISK = (
       (INNE, ('Inne')),
       (ŻYWNOŚĆ, ('Żywność')),
       (CIUCHY, ('Ciuchy')),
    )

    rodzaj_stoiska = models.PositiveSmallIntegerField(
        choices = RODZAJE_STOISK,
        default = INNE
    )
    czy_aktywne = models.BooleanField()
    opis_stanowiska = models.CharField(max_length=256)
    krotki_opis = models.CharField(max_length = 60, default="Krótki opis stanowiska")
    zdjecie = models.ImageField(upload_to= 'stoiska_zdjecia')
    sprzedawca = models.ForeignKey(Sprzedawca, blank=True, null=True, on_delete= models.SET_NULL)
    wspolrzedne_x = models.FloatField(null=False)
    wspolrzedne_y = models.FloatField(null=False)



    def __str__(self):
        return  "Stoisko {numer}".format(numer = self.id)       
    

class Produkt(models.Model):
    
    id = models.AutoField(primary_key=True)
    nazwa_stoiska = models.ForeignKey(Stoisko, on_delete=models.CASCADE)
    nazwa_produktu = models.CharField(max_length=40)

    
    def __str__(self):
        return self.nazwa_produktu

# query = Stoisko.objects.filter(id = 1)

# if query.exists == False: 
#     moje_stoisko = Stoisko(id = 1, rodzaj_stoiska = "żywność", czy_aktywne = True, krotki_opis = 'ale opis', opis_stanowiska = "Świeże produkty prosto z pola w Pieszycach. Dobre, bo swojskie :)", ocena = 5)
#     moje_stoisko.save()

# query = Produkt.objects.filter(id = 1)

# if query.exists == False: 
#     moj_produkt = Produkt(nazwa_stoiska = moje_stoisko, nazwa_produktu = 'banan', rodzaj_produktu = 'żywność', ilosc = 2)
#     moj_produkt.save()