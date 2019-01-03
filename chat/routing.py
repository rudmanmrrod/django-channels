"""
Django Realtime Chat & Notifications
"""
## @package chat.routing
#
# Urls de la aplicación participacion
# @version 1.0
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('chat/', consumers.ChatConsumer),
]