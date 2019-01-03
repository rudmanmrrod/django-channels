"""
Django Realtime Chat & Notifications
"""
## @package users.urls
#
# Urls de la aplicación participacion
# @version 1.0
from django.urls import path
from .views import *

app_name = 'base'
urlpatterns = [
    path('', Inicio.as_view(), name = "inicio")
]