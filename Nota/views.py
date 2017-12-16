from django.shortcuts import render,redirect
from Nota.forms import NotaForm
from Nota.models import Nota


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Crear en funciones.
@login_required(login_url='/')
def index(request):
    # return HttpResponse("index")
    return render(request, 'nota/index.html')

#***************   BASADA EN CLASES *************
# REGISTRAR
class NotaCreate(LoginRequiredMixin, CreateView):
    model = Nota
    form_class = NotaForm
    template_name = 'nota/nota_registrar.html'
    success_url = reverse_lazy('nota:nota_listar')
# LISTAR
class NotaList(LoginRequiredMixin, ListView):
    model = Nota
    template_name = 'nota/nota_listar.html'
#ACTUALIZAR
class NotaUpdate(LoginRequiredMixin, UpdateView):
    model = Nota
    form_class = NotaForm
    template_name = 'nota/nota_registrar.html'
    success_url = reverse_lazy('nota:nota_listar')
#Eliminar
class NotaDelete(LoginRequiredMixin, DeleteView):
    model = Nota
    template_name = 'nota/nota_delete.html'
    success_url = reverse_lazy('nota:nota_listar')
# Reportes
class NotaReport(LoginRequiredMixin, ListView):
    model = Nota
    template_name = 'nota/nota_reportes.html'