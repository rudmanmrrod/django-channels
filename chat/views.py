"""
Django Realtime Chat & Notifications
"""
## @package chat.views
#
# Vistas correspondientes a la aplicación chat
# @author Leonel Hernández (leonelphm at gmail)
# @author Rodrigo Boet (rudmanmrrod at gmail)
# @version 1.0
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from django.views.generic import FormView

from .forms import ChatSendForm
from .models import Comentario


class ChatView(LoginRequiredMixin, FormView):
    """!
    Clase que gestiona la vista del chat

    @date 07-03-2018
    @version 1.0.0
    """
    template_name = "chat.template.html"
    form_class = ChatSendForm

    def get_context_data(self, **kwargs):
        """!
        Metodo que permite cargar de nuevo valores en los datos de contexto de la vista

        @date 07-03-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param kwargs <b>{object}</b> Objeto que contiene los datos de contexto
        @return Retorna los datos de contexto
        """
        kwargs['users'] = User.objects.exclude(username=self.request.user.username).all()
        return super().get_context_data(**kwargs)

class ListComment(View):
    """!
    Clase que gestiona la lista de los comentarios

    @date 07-03-2018
    @version 1.0.0
    """
    def get(self, request, **kwargs):
        usuario_emite = request.user.pk
        usuario_recibe = request.GET.get('user_reci')
        serialized_object = None
        if usuario_emite is not None and usuario_recibe is not None:
            comentarios = Comentario.objects.filter(
                Q(fk_user_emite=usuario_emite, fk_user_recibe=usuario_recibe)  |  
                Q(fk_user_emite=usuario_recibe,fk_user_recibe=usuario_emite)).all(
                ).order_by('fecha')
            serialized_object = serializers.serialize('json', comentarios)

        return JsonResponse(serialized_object, safe=False)


class AddComment(View):
    """!
    Clase que gestiona el agregardo de los comentarios

    @date 07-03-2018
    @version 1.0.0
    """
    def post(self, request, **kwargs):
        comentario = request.POST.get('comentario')
        usuario_emite = request.POST.get('user_emite')
        usuario_recibe = request.POST.get('user_recibe')
        try:
            user_rec = User.objects.get(pk=usuario_recibe)
            user_emit = User.objects.get(pk=usuario_emite)
        except Exception as e:
            print(e)
            user_rec = None
            user_emit = None
        serialized_object = None
        if usuario_emite is not None and usuario_recibe is not None:
            try:
                comment = Comentario()
                comment.fk_user_emite = user_emit
                comment.fk_user_recibe = user_rec
                comment.comentario = comentario
                comment.save()
                serialized_object = serializers.serialize('json', [comment])
            except Exception as e:
                print(e)
                serialized_object = {'error': 'Fallo el envio de mensaje'}

        return JsonResponse(serialized_object, safe=False)