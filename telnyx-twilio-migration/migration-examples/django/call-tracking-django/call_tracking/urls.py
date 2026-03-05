from django.urls import re_path

from .views import (
    list_numbers,
    purchase_number,
    forward_call,
    LeadSourceUpdateView,
    leads_by_source,
    leads_by_city,
)

urlpatterns = [
    # URLs for searching for and purchasing a new Twilio number
    re_path(r'^list-numbers$', list_numbers, name='list_numbers'),
    re_path(r'^purchase-number$', purchase_number, name='purchase_number'),
    # Endpoint Twilio will use for incoming calls
    re_path(r'^forward-call$', forward_call, name='forward_call'),
    # Lead Source edit and delete views
    re_path(
        r'^(?P<pk>[0-9]+)/edit$',
        LeadSourceUpdateView.as_view(),
        name='edit_lead_source',
    ),
    # JSON URLs for the bar chart data
    re_path(r'^leads-by-source$', leads_by_source, name='leads_by_source'),
    re_path(r'^leads-by-city$', leads_by_city, name='leads_by_city'),
]
