from django.contrib import admin

from .models import LeadSource, Lead

# Register our models with the basic ModelAdmin
admin.site.register(LeadSource, admin.ModelAdmin)
admin.site.register(Lead, admin.ModelAdmin)
