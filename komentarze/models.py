from django.db import models
from stoisko.models import Stoisko
from main.models import User
from django.contrib.humanize.templatetags import humanize
from datetime import datetime

class Komentarz(models.Model):
    stoisko = models.ForeignKey(Stoisko,on_delete=models.CASCADE,related_name='komentarze')
    kreator = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)
    tekst = models.CharField(max_length=400)
    stworzono = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['stworzono']

    def __str__(self):
        return 'Treść: {} \n Twórca: {}'.format(self.tekst, self.kreator)

    def time_since_PL(self):
        czas = humanize.naturaltime(self.stworzono)
        str(czas)

    # I know that there's a way to do some cool translation stuff with messages n' all that but i need this thing done fast  and I swear on my pinkie if there's
    # more translations to do i'll do it properly
    @property
    def pretty_date_PL(self):

        now = datetime.now()
        stworzono = self.stworzono.replace(tzinfo=None)

        diff = now - stworzono
        second_diff = diff.seconds
        day_diff = diff.days

        if day_diff < 0:
            return ''

        if day_diff == 0:
            if second_diff < 10:
                return "w tej chwili"
            if second_diff < 60:
                return str(second_diff) + " sek temu"
            if second_diff < 120:
                return "minutę temu"
            if second_diff < 3600:
                return str(second_diff // 60) + " min temu"
            if second_diff < 7200:
                return "godzinę temu"
            if second_diff < 86400:
                return str(second_diff // 3600) + " godz temu"
        if day_diff == 1:
            return "Wczoraj"
        if day_diff < 7:
            return str(day_diff) + " dni temu"
        if day_diff < 31:
            return str(day_diff // 7) + " tygodni temu"
        if day_diff < 365:
            return str(day_diff // 30) + " miesięcy temu"
        return str(day_diff // 365) + " lat temu"

            

# Create your models here.
