from django.conf.urls import url
from .views import CountryAutocomplete, PersonCreateView

urlpatterns = [
    url(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete'),
    url(r'^person/create/$', PersonCreateView.as_view(), name='create-person'),
]
