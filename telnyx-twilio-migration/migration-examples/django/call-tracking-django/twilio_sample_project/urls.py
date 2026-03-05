from django.urls import include, re_path
from django.contrib import admin

from call_tracking.views import home

urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^call-tracking/', include('call_tracking.urls')),

    # Include the Django admin
    re_path(r'^admin/', admin.site.urls),
]
