"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from Usuario.views import LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alumno/', include('Alumno.urls', namespace='alumno')),
    url(r'^docente/', include('Docente.urls', namespace='docente')),
    url(r'^curso/', include('Curso.urls', namespace='curso')),
    url(r'^nota/', include('Nota.urls', namespace='nota')),
    url(r'^especialidad/', include('Especialidad.urls', namespace='especialidad')),
    url(r'^categoria/', include('Categoria.urls', namespace='categoria')),
    url(r'^matricula/', include('Matricula.urls', namespace='matricula')),
    url(r'^usuario/', include('Usuario.urls', namespace='usuario')),

    url(r'^$', auth_views.LoginView.as_view(template_name='index.html'), name='auth_login'),
    url(r'^logout/$', LogoutView.as_view(), name='auth_logout')

]
