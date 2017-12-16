# Create your views here.
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from Usuario.serializers import UserSerializer

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, RedirectView

from Usuario.forms import RegistroForm

# API JSON
class UserApi(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
# logout
class LogoutView(RedirectView):
    permanent = False
    query_string = True
    url = '/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            auth_logout(request)
        return super().get(request, *args, **kwargs)


class RegistroUusario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'usuario/usuario_registrar.html'
    success_url = reverse_lazy('usuario:registro_listar')


class RegistroList(ListView):
    model = User
    template_name = 'usuario/usuario_listar.html'


# ACTUALIZAR
class RegistroUpdate(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = 'usuario/usuario_registrar.html'
    success_url = reverse_lazy('usuario:registro_listar')


# Eliminar
class RegistroDelete(DeleteView):
    model = User
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario:registro_listar')


# Reportes
class RegistroReport(ListView):
    model = User
    template_name = 'usuario/usuario_reportes.html'
