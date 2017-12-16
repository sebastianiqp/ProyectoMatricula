from django.shortcuts import render, redirect
from Alumno.forms import AlumnoForm


from Alumno.models import Alumno
from rest_framework.views import APIView
from Alumno.serializers import AlumnoSerializer
from rest_framework.response import Response

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# API JSON
class AlumnoApi(APIView):
    def get(self, request, format=None):
        Alu = Alumno.objects.all()
        serializer = AlumnoSerializer(Alu, many=True)
        return Response(serializer.data)

# Crear en funciones.
@login_required(login_url='/')
def index(request):
    # return HttpResponse("index")
    return render(request, 'alumno/index.html')

# ***************   BASADA EN CLASES *************
# REGISTRAR
class AlumnoCreate(LoginRequiredMixin, CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno/alumno_registrar.html'
    success_url = reverse_lazy('alumno:alumno_listar')

# LISTAR
class AlumnoList(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = 'alumno/alumno_listar.html'

# ACTUALIZAR
class AlumnoUpdate(LoginRequiredMixin, UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno/alumno_registrar.html'
    success_url = reverse_lazy('alumno:alumno_listar')

# Eliminar
class AlumnoDelete(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = 'alumno/alumno_delete.html'
    success_url = reverse_lazy('alumno:alumno_listar')

# Reportes
class AlumnoReport(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = 'alumno/alumno_reportes.html'
