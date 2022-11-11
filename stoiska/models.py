from django.db import models

# Create your models here.

class Stoisko(models.Model):

    stoisko_id = models.IntegerField()
    rodzaj_stoiska = models.CharField(max_length=25)
    czy_aktywne = models.BinaryField()
    opis_stanowiska = models.CharField(max_length=256)
    ocena = models.PositiveIntegerField()


    def __str__(self):
        return self.stoisko_id
    
