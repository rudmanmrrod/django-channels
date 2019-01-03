from django.contrib.auth.mixins import LoginRequiredMixin
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