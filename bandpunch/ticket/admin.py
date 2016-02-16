from django.contrib import admin
from ticket.models import Venue, Event, Artist, UserAccount, Purchase, Genre, CardChoices
from ticket.forms import PurchaseForm

# Classes which allow management of different tables in the database with support for filtering.
admin.site.register(Genre)
admin.site.register(CardChoices)

class VenueAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'address', 'capacity', 'phone_number', 'website')
    list_filter = [ "capacity" ]
    prepopulated_fields = {'slug':('name',)}
    search_fields = [ "name", "address" ]
admin.site.register(Venue, VenueAdmin)

class EventAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name', 'price', 'date', 'start_time')
	list_filter = [ "name", "date", "start_time", "price" ]
	prepopulated_fields = {'slug':('name',)}
	search_fields = [ "venues", "name" ]
admin.site.register(Event, EventAdmin)

class ArtistAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name', 'genre')
	list_filter = [ "name", "genre" ]
	prepopulated_fields = {'slug':('name',)}
	search_fields = [ "name", "description"]
admin.site.register(Artist, ArtistAdmin)

class UserAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name', 'address', 'phone_number', 'email')
	list_filter = [ "name" ]
	search_fields = [ "name", "address", "phone_number", "email" ]
admin.site.register(UserAccount, UserAdmin)

class PurchaseAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('cash_only', 'card_name', 'payment_type', 'card_number', 'date', 'delivery_option', 'reference_number')
	list_filter = [ "payment_type" ]
	search_fields = [ "card_number", "card_name" ]
	
	def get_readonly_fields(self, request, obj=None): # Display readonly fields
		if obj:
			return [ "date", "reference_number" ]
		return self.readonly_fields

admin.site.register(Purchase, PurchaseAdmin)