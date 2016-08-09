from django.contrib import admin
from .models import Event, Ticket


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_creation', 'date_update', 'visibility', 'paying')
    search_fields = ('title', 'description')

    fieldsets = (
        ('General', {
            'fields': ('title', 'location', 'author', 'link', 'image', 'height_field', 'width_field', 'date_start', 'date_end', )
        }),
        # Fieldset 2
        ('Description', {
           'description': 'The form handle the HTML balise. Use them wisely!',
           'fields': ('description', )
        }),
        # Fieldset 3
        ('Contact & other', {
           'fields': ('mail', 'visibility', 'paying')
        }),
    )
    # prepopulated_fields = {'slug': ('title', ), }


class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ('name', 'price', 'get_title', )
    search_fields = ('name', 'get_title')
    fieldsets = (
        # Fieldset 1: meta-info (title, location, ..)
        ('General', {
            'fields': ('name', 'event_id')
        }),
        # Fieldset 2
        ('Price & Quantity', {
           'fields': ('price', 'quantity', 'sold', )
        }),
    )

    def get_title(self, obj):
        return obj.event_id.title
    get_title.admin_order_field = 'event_id'
    get_title.short_description = 'Event Name'

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Event, EventAdmin)
