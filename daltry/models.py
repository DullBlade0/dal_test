from django.db import models

# Create your models here.
class Country(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    country_code = models.CharField(max_length=10)


    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=120)
    home_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='home_country')
    visited_countries = models.ManyToManyField(Country)

    def __str__(self):
        return self.name