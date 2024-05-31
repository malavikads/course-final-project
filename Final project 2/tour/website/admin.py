from django.contrib import admin
from.models import Listtour,Vendorf

class Alisttour(admin.ModelAdmin):
    list_display = ('name','departure_date','accomodation','transportation','duration','cost','activities','climate')


admin.site.register(Listtour,Alisttour)

class Avendorf(admin.ModelAdmin):
    list_display = ('name_of_vendor','visiting_place','duration','departure_date', 'accomodation','transportation','contact_no',)


admin.site.register(Vendorf,Avendorf)
