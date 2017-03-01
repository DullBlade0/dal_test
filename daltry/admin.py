from django.contrib import admin
from import_export import resources, fields

from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from .models import Country, Person
from .forms import PersonForm


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country


class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource

class PersonAdmin(admin.ModelAdmin):
    form = PersonForm

admin.site.register(Country, CountryAdmin)
admin.site.register(Person, PersonAdmin)
