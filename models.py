from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Movies(models.Model):
    MY_CHOICES = ((1, 'Happy'),
              (2, 'Average'),
              (3, 'Sad'),
              )
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    genre1 = models.CharField(max_length=100,blank=True,null=True)
    laenge = models.CharField(max_length=100)
    jahr = models.CharField(max_length=100,null=True,blank=True)
    regie = models.CharField(max_length=100)
    imdb_rating = models.CharField(max_length=100)
    funny_film = models.CharField(max_length=100,null=True,blank=True)
    sad_film = models.CharField(max_length=100,null=True,blank=True)
    film_intense = models.CharField(max_length=100,null=True,blank=True)
    #mood_rating = models.CharField(max_length=100,null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=1,
                         max_length=30,null=True,blank=True)

    def __str__(self):
        return self.name
    #
    # def save(self,*args,**kwargs):
    #     flim_lusting=0
    #     flim_trauring=0
    #     mood_rating=0
    #     evaluation = abs(flim_lusting-flim_trauring)
    #     result = (10 - evaluation)
    #     result = mood_rating
    #     super(Movies,self).save(*args,**kwargs)
