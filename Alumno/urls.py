from django.conf.urls import url, include
from Alumno.views import index, AlumnoList, AlumnoCreate, AlumnoUpdate, AlumnoDelete, AlumnoReport, AlumnoApi

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo_alumno$', AlumnoCreate.as_view(), name='alumno_crear'),
    url(r'^listar_alumno$', AlumnoList.as_view(), name='alumno_listar'),
    url(r'^editar_alumno/(?P<pk>\d+)/$', AlumnoUpdate.as_view(), name='alumno_editar'),
    url(r'^eliminar_alumno/(?P<pk>\d+)/$', AlumnoDelete.as_view(), name='alumno_eliminar'),

    url(r'^reportes_alumno$', AlumnoReport.as_view(), name='alumno_reportes'),

    url(r'^api$', AlumnoApi.as_view(), name='api'),
]
