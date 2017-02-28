from dal import autocomplete

from django import forms

from .models import *


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('name', )
        widgets = {
            'home_country': autocomplete.ModelSelect2(url='country-autocomplete'),
            'visited_countries': autocomplete.ModelSelect2Multiple(url='country-autocomplete')
        }
