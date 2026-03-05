from django.urls import path

from . import views

app_name = 'ivr'

urlpatterns = [
    path('', views.index, name='index'),
    path('agents/', views.agents, name='agents'),
    path('welcome/', views.welcome, name='welcome'),
    path('menu/', views.menu, name='menu'),
    path('agent/connect', views.agent_connect, name='agent_connect'),
    path('agent/screencall', views.screencall, name='agents_screencall'),
    path('agent/connect_message', views.connect_message, name='agents_connect_message'),
    path('agent/call', views.agent_call, name='agents_call'),
    path('agent/hangup', views.hangup, name='hangup'),
    path('agent/recordings', views.recordings, name='recordings'),
]
