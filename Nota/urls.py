from django.conf.urls import url, include
from Nota.views import  index, NotaList, NotaCreate, NotaUpdate, NotaDelete, NotaReport

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo_nota$', NotaCreate.as_view(), name='nota_crear'),
    url(r'^listar_nota$', NotaList.as_view(), name='nota_listar'),
    url(r'^editar_nota/(?P<pk>\d+)/$', NotaUpdate.as_view(), name='nota_editar'),
    url(r'^eliminar_anota/(?P<pk>\d+)/$', NotaDelete.as_view(), name='nota_eliminar'),

    url(r'^reportes_nota$', NotaReport.as_view(), name='nota_reportes'),

]
