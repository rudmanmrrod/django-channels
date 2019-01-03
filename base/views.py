"""
Django Realtime Chat & Notifications
"""
## @package base.views
#
# Vistas correspondientes a la aplicación base
# @version 1.0
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

    
class Inicio(LoginRequiredMixin,TemplateView):
    """!
    Clase para mostrar el inicio del sistema

    @date 24-04-2017
    @version 1.0.0
    """
    template_name = "inicio.html"