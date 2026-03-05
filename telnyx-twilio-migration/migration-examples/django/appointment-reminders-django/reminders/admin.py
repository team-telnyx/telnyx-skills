from django.contrib import admin

from .models import Appointment

# Register our Appointment model with the basic ModelAdmin
admin.site.register(Appointment, admin.ModelAdmin)
