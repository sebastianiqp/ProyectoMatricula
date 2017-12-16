from django.conf.urls import url, include
from Curso.views import  index, CursoList, CursoCreate, CursoUpdate, CursoDelete, CursoReport

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo_curso$', CursoCreate.as_view(), name='curso_crear'),
    url(r'^listar_curso$', CursoList.as_view(), name='curso_listar'),
    url(r'^editar_curso/(?P<pk>\d+)/$', CursoUpdate.as_view(), name='curso_editar'),
    url(r'^eliminar_curso/(?P<pk>\d+)/$', CursoDelete.as_view(), name='curso_eliminar'),

    url(r'^reportes_curso$', CursoReport.as_view(), name='curso_reportes'),



]
