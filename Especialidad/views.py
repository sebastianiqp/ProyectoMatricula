from django.shortcuts import render,redirect
from Especialidad.forms import EspecialiadadForm
from Especialidad.models import Especialidad

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Crear en funciones.
@login_required(login_url='/')
def index(request):
    # return HttpResponse("index")
    return render(request, 'especialidad/index.html')

#***************   BASADA EN CLASES *************
# REGISTRAR
class EspecialidadCreate(LoginRequiredMixin, CreateView):
    model = Especialidad
    form_class = EspecialiadadForm
    template_name = 'especialidad/especialidad_registrar.html'
    success_url = reverse_lazy('especialidad:especialidad_listar')
# LISTAR
class EspecialidadList(LoginRequiredMixin, ListView):
    model = Especialidad
    template_name = 'especialidad/especialidad_listar.html'
#ACTUALIZAR
class EspecialidadUpdate(LoginRequiredMixin, UpdateView):
    model = Especialidad
    form_class = EspecialiadadForm
    template_name = 'especialidad/especialidad_registrar.html'
    success_url = reverse_lazy('especialidad:especialidad_listar')
#Eliminar
class EspecialidadDelete(LoginRequiredMixin, DeleteView):
    model = Especialidad
    template_name = 'especialidad/especialidad_delete.html'
    success_url = reverse_lazy('especialidad:especialidad_listar')
# Reportes
class EspecialidadReport(LoginRequiredMixin, ListView):
    model = Especialidad
    template_name = 'especialidad/especialidad_reportes.html'