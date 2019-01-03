"""
Django Realtime Chat & Notifications
"""
## @package users.urls
#
# Urls de la aplicación participacion
# @version 1.0
from django.urls import path
from .views import *
from users import views

app_name = 'users'
urlpatterns = [
    path('login', LoginView.as_view(), name = "login"),
    path('logout', LogoutView.as_view(), name = "logout"),
    path('register', RegisterView.as_view(), name = "register"),
]
