from django.shortcuts import render,redirect
from Docente.forms import DocenteForm
from Docente.models import Docente


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Crear en funciones.
@login_required(login_url='/')
def index(request):
    # return HttpResponse("index")
    return render(request, 'docente/index.html')
#***************   BASADA EN CLASES *************
# REGISTRAR
class DocenteCreate(LoginRequiredMixin, CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'docente/docente_registrar.html'
    success_url = reverse_lazy('docente:docente_listar')
# LISTAR
class DocenteList(LoginRequiredMixin, ListView):
    model = Docente
    template_name = 'docente/docente_listar.html'
#ACTUALIZAR
class DocenteUpdate(LoginRequiredMixin, UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'docente/docente_registrar.html'
    success_url = reverse_lazy('docente:docente_listar')
#Eliminar
class DocenteDelete(LoginRequiredMixin, DeleteView):
    model = Docente
    template_name = 'docente/docente_delete.html'
    success_url = reverse_lazy('docente:docente_listar')
# Reportes
class DocenteReport(LoginRequiredMixin, ListView):
    model = Docente
    template_name = 'docente/docente_reportes.html'