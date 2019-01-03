"""
Django Realtime Chat & Notifications
"""
## @package chat.urls
#
# Urls de la aplicación participacion
# @version 1.0
from django.urls import path
from .views import *

app_name = 'chat'
urlpatterns = [
    path('', ChatView.as_view(), name = "chat"),
    
]