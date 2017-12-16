from django.conf.urls import url, include
from Especialidad.views import  index, EspecialidadList, EspecialidadCreate, EspecialidadUpdate, EspecialidadDelete, EspecialidadReport

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo_especialidad$', EspecialidadCreate.as_view(), name='especialidad_crear'),
    url(r'^listar_especialidad$', EspecialidadList.as_view(), name='especialidad_listar'),
    url(r'^editar_especialidad/(?P<pk>\d+)/$', EspecialidadUpdate.as_view(), name='especialidad_editar'),
    url(r'^eliminar_especialidad/(?P<pk>\d+)/$', EspecialidadDelete.as_view(), name='especialidad_eliminar'),

    url(r'^reportes_especialidad$', EspecialidadReport.as_view(), name='especialidad_reportes'),

]
