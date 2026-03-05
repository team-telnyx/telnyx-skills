from django.conf.urls import re_path

from .views import (
    AppointmentCreateView,
    AppointmentDeleteView,
    AppointmentDetailView,
    AppointmentListView,
    AppointmentUpdateView,
)

app_name = 'reminders'

urlpatterns = [
    # List and detail views
    re_path(r'^$', AppointmentListView.as_view(), name='list_appointments'),
    re_path(r'^(?P<pk>[0-9]+)$',
            AppointmentDetailView.as_view(),
            name='view_appointment'),

    # Create, update, delete
    re_path(r'^new$', AppointmentCreateView.as_view(), name='new_appointment'),
    re_path(r'^(?P<pk>[0-9]+)/edit$',
            AppointmentUpdateView.as_view(),
            name='edit_appointment'),
    re_path(r'^(?P<pk>[0-9]+)/delete$',
            AppointmentDeleteView.as_view(),
            name='delete_appointment'),
]
