from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    first_name = None
    last_name = None
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        UZYTKOWNIK = "UZYTKOWNIK", "Uzytkownik"
        SPRZEDAWCA = "SPRZEDAWCA", "Sprzedawca"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)




class UzytkownikManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.UZYTKOWNIK)


class Uzytkownik(User):

    base_role = User.Role.UZYTKOWNIK
    uzytkownik = UzytkownikManager()

    class Meta:
        proxy = True

class SprzedawcaManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SPRZEDAWCA)
    
    


class Sprzedawca(User):

    base_role = User.Role.SPRZEDAWCA
    sprzedawca = SprzedawcaManager()


    class Meta:
        proxy = True



# Create your models here.

class SprzedawcaProfile(models.Model):
    user = models.OneToOneField(Sprzedawca, on_delete=models.CASCADE, primary_key=True)
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)

    def __str__(self):
        return self.imie



@receiver(post_save, sender=Sprzedawca)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "SPRZEDAWCA":
        SprzedawcaProfile.objects.create(user=instance)


