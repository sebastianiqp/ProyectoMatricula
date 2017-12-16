from django.conf.urls import url, include
from Matricula.views import index, MatriculaList, MatriculaCreate, MatriculaUpdate, MatriculaDelete, MatriculaReport

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo_matricula$', MatriculaCreate.as_view(), name='matricula_crear'),
    url(r'^listar_matricula$', MatriculaList.as_view(), name='matricula_listar'),
    url(r'^editar_matricula/(?P<pk>\d+)/$', MatriculaUpdate.as_view(), name='matricula_editar'),
    url(r'^eliminar_matricula/(?P<pk>\d+)/$', MatriculaDelete.as_view(), name='matricula_eliminar'),

    url(r'^reportes_matricula$', MatriculaReport.as_view(), name='matricula_reportes'),

]
