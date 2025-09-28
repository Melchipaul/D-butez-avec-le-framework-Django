from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=5, choices=Genre.choices)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), 
                    MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Listing(models.Model):
    class Type(models.TextChoices):
        DISQUES = 'Records'
        VETEMENTS = 'Clothing'
        AFFICHES = 'Posters'
        DIVERS = 'Miscellaneous'
    title = models.fields.CharField(max_length=200)
    description = models.fields.CharField(max_length=2000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    type = models.fields.CharField(max_length=20, choices=Type.choices)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
