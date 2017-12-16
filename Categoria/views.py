from django.shortcuts import render,redirect
from Categoria.forms import CategoriaForm


from Categoria.models import Categoria
from rest_framework.views import APIView
from Categoria.serializers import CategoriaSerializer
from rest_framework.response import Response


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class CategoriaApi(APIView):
    def get(self, request):
        cate = Categoria.objects.all()
        serializer = CategoriaSerializer(cate, many=True)
        return Response(serializer.data)




# Create your views here.
@login_required(login_url='/')
def index(request):
    # return HttpResponse("index")
    return render(request, 'categoria/index.html')

#***************   BASADA EN CLASES *************
# REGISTRAR
class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_registrar.html'
    success_url = reverse_lazy('categoria:categoria_listar')
# LISTAR
class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria/categoria_listar.html'
#ACTUALIZAR
class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_registrar.html'
    success_url = reverse_lazy('categoria:categoria_listar')
#Eliminar
class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_delete.html'
    success_url = reverse_lazy('categoria:categoria_listar')
# Reportes
class CategoriaReport(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria/categoria_reportes.html'