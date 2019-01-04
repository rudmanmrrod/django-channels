"""django_channels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    PasswordResetConfirmView, PasswordResetCompleteView
    )
from users.forms import PasswordConfirmForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls', namespace="base")),
    path('', include('users.urls')),
    path('chat/', include('chat.urls')),
    path('user/password/reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='user.passwordreset.confirm.html',
                                        success_url='/user/password/done/',
                                        form_class=PasswordConfirmForm
                                        ),
        name='password_reset_confirm',
    ),
    path(
        'user/password/done/',
        PasswordResetCompleteView.as_view(template_name='user.passwordreset.end.html'),
        name='pass_done',
    ),
]
