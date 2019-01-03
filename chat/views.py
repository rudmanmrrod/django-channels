from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import FormView

from .forms import ChatSendForm


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