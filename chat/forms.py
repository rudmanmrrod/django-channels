"""
Django Realtime Chat & Notifications
"""
## @package chat.forms
#
# Formularios correspondientes a la aplicación chat
# @version 1.0
from django import forms

class ChatSendForm(forms.Form):
  """!
  Clase que gestiona el formulario del envio en el chat

  @date 07-03-2018
  @version 1.0.0
  """ 

  ## Mensaje
  comentario = forms.CharField()