from django.shortcuts import render,redirect
from Curso.forms import CursoForm
from Curso.models import Curso


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Crear en funciones.
@login_required(login_url='/')
def index(request):
    # return HttpResponse("index")
    return render(request, 'curso/index.html')
#***************   BASADA EN CLASES *************
# REGISTRAR
class CursoCreate(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_registrar.html'
    success_url = reverse_lazy('curso:curso_listar')
# LISTAR
class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'curso/curso_listar.html'
#ACTUALIZAR
class CursoUpdate(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_registrar.html'
    success_url = reverse_lazy('curso:curso_listar')
#Eliminar
class CursoDelete(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'curso/curso_delete.html'
    success_url = reverse_lazy('curso:curso_listar')

# Reportes
class CursoReport(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'curso/curso_reportes.html'