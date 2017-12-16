from django.conf.urls import url, include
from Docente.views import  index, DocenteList, DocenteCreate, DocenteUpdate, DocenteDelete, DocenteReport

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo_docente$', DocenteCreate.as_view(), name='docente_crear'),
    url(r'^listar_docente$', DocenteList.as_view(), name='docente_listar'),
    url(r'^editar_docente/(?P<pk>\d+)/$', DocenteUpdate.as_view(), name='docente_editar'),
    url(r'^eliminar_docente/(?P<pk>\d+)/$', DocenteDelete.as_view(), name='docente_eliminar'),

    url(r'^reportes_docente$', DocenteReport.as_view(), name='docente_reportes'),

]
