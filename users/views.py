"""
Django Realtime Chat & Notifications
"""
## @package user.views
#
# Vistas correspondientes a la aplicación usuario
# @version 1.0
from django.shortcuts import render, redirect
from django.views.generic import (
    FormView, RedirectView, CreateView, 
    UpdateView, ListView, TemplateView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.http import HttpResponseForbidden, JsonResponse
from .forms import (
    LoginForm, UserRegisterForm, 
    PasswordChangeForm
    )



class LoginView(FormView):
    """!
    Clase que gestiona la vista principal del logeo de usuario

    @date 01-03-2017
    @version 1.0.0
    """
    form_class = LoginForm
    template_name = 'user.login.html'
    success_url = reverse_lazy('base:inicio')

    def form_valid(self, form):
        """!
        Metodo que valida si el formulario es valido
    
        @date 01-03-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de registro
        @return Retorna el formulario validado
        """
        usuario = form.cleaned_data['usuario']
        contrasena = form.cleaned_data['contrasena']
        usuario = authenticate(username=usuario, password=contrasena)
        login(self.request, usuario)
        if self.request.POST.get('remember_me') is not None:
            # Session expira a los dos meses si no se deslogea
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)
    
    
class LogoutView(RedirectView):
    """!
    Clase que gestiona la vista principal del deslogeo de usuario

    @date 01-03-2017
    @version 1.0.0
    """
    permanent = False
    query_string = True

    def get_redirect_url(self):
        """!
        Metodo que permite definir la url de dirección al ser válido el formulario
    
        @date 01-03-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la url
        """
        logout(self.request)
        return reverse_lazy('users:login')


class RegisterView(SuccessMessageMixin,CreateView):
    """!
    Muestra el formulario de registro de usuarios

    @date 09-01-2017
    @version 1.0.0
    """
    template_name = "user.register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('base:inicio')
    success_message = "Se registró con éxito"
    model = User


class ChangePasswordView(LoginRequiredMixin,TemplateView):
    """!
    Clase que gestiona el borrado de una pregunta

    @date 20-02-2018
    @version 1.0.0
    """
    template_name = "change_password.form.html"
    
    def post(self, request):
        """!
        Metodo que sobreescribe la acción por POST
    
        @date 20-02-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param pk <b>{int}</b> Recibe el id del perfil
        @return Retorna los datos de contexto
        """
        perfil = Perfil.objects.filter(user_id=int(request.user.id))
        if perfil:
            perfil = perfil.get()
            old_p = request.POST.get('old_password','')
            new_p = request.POST.get('new_password','')
            new_rp = request.POST.get('new_password_repeat','')
            if old_p=='' or new_p=='' or new_rp=='':
                return JsonResponse({'success':False,'mensaje':'Datos Vacíos'})
            elif new_p != new_rp:
                return JsonResponse({'success':False,'mensaje':'Las contraseñas no coinciden'})
            elif not check_password(old_p,perfil.user.password):
                return JsonResponse({'success':False,'mensaje':'La contraseña anterior es inválida'})
            else:
                perfil.user.set_password(new_p)
                perfil.user.save()
                return JsonResponse({'success':True,'mensaje':'Se cambió la contraseña con éxito'})
        else:
            return JsonResponse({'success':False,'mensaje':'Perfil Invalido'})

