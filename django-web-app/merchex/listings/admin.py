from django.contrib import admin

from listings.models import Band, Listing
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'year', 'band', 'sold')
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
