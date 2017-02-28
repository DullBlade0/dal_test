from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse

from dal import autocomplete

from pruebas.models import Country, Person
from pruebas.forms import PersonForm


# Create your views here.

class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Country.objects.none()
        qs = Country.objects.all()
        # What is self.q ?
        if self.q:
            # is there a way to filter this using self.request.user.profile if it existed?
            qs = qs.filter(name__istartswith=self.q)
        return qs

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'form.html'
    # success_url = reverse('create-person')