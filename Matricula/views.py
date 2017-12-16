from django.shortcuts import render,redirect
from Matricula.forms import MatriculaForm
from Matricula.models import Matricula

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Crear en funciones.
@login_required(login_url='/')
def index(request):
    # return HttpResponse("index")
    return render(request, 'matricula/index.html')

#***************   BASADA EN CLASES *************
# REGISTRAR
class MatriculaCreate(LoginRequiredMixin, CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula/matricula_registrar.html'
    success_url = reverse_lazy('matricula:matricula_listar')
# LISTAR
class MatriculaList(LoginRequiredMixin, ListView):
    model = Matricula
    template_name = 'matricula/matricula_listar.html'
#ACTUALIZAR
class MatriculaUpdate(LoginRequiredMixin, UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula/matricula_registrar.html'
    success_url = reverse_lazy('matricula:matricula_listar')
#Eliminar
class MatriculaDelete(LoginRequiredMixin, DeleteView):
    model = Matricula
    template_name = 'matricula/matricula_delete.html'
    success_url = reverse_lazy('matricula:matricula_listar')
# Reportes
class MatriculaReport(LoginRequiredMixin, ListView):
    model = Matricula
    template_name = 'matricula/matricula_reportes.html'