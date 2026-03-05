from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^automated-survey/', include('automated_survey.urls')),
    path('', lambda r: redirect('/automated-survey/'), name='root-redirect')
]
