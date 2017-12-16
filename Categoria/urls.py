from django.conf.urls import url, include
from Categoria.views import index, CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete, CategoriaReport, CategoriaApi

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo_categoria$', CategoriaCreate.as_view(), name='categoria_crear'),
    url(r'^listar_categoria$', CategoriaList.as_view(), name='categoria_listar'),
    url(r'^editar_categoria/(?P<pk>\d+)/$', CategoriaUpdate.as_view(), name='categoria_editar'),
    url(r'^eliminar_categoria/(?P<pk>\d+)/$', CategoriaDelete.as_view(), name='categoria_eliminar'),

    url(r'^reportes_categoria$', CategoriaReport.as_view(), name='categoria_reportes'),

    url(r'^api$', CategoriaApi.as_view(), name='api'),

]
