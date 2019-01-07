"""
Django Realtime Chat & Notifications
"""
## @package chat.models
#
# Modelos de la aplicación chat
# @author Leonel Hernández (leonelphm at gmail)
# @author Rodrigo Boet (rudmanmrrod at gmail)
# @version 1.0
from django.contrib.auth.models import User
from django.db import models

class Comentario(models.Model):
    """!
    Clase que contiene los datos de los Comentarios

    @author Ing. Leonel P. Hernandez M. (leonelphm at gmail)
    @copyright MIT
    @date 07-03-2018
    @version 1.0.0
    """
    fk_user_emite = models.ForeignKey(User, related_name='usurio_emite', on_delete=models.CASCADE)
    fk_user_recibe = models.ForeignKey(User, related_name='usurio_recibe', on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    visto = models.BooleanField(default=False)

    class Meta:
        """!
            Clase que construye los meta datos del modelo
        """
        ordering = ('fecha',)
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        db_table = 'chat_comentario'

    def __str__(self):
        """!
        Función que muestra el comentario

        @return Devuelve el comentario
        """
        return self.comentario