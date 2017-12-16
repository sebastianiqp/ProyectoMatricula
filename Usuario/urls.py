from django.conf.urls import url, include
from Usuario.views import RegistroUusario, RegistroList, RegistroUpdate, RegistroDelete, RegistroReport, UserApi

urlpatterns = [
    url(r'^nuevo_registro$', RegistroUusario.as_view(), name='registro_crear'),
    url(r'^listar_registro$', RegistroList.as_view(), name='registro_listar'),

    url(r'^editar_registro/(?P<pk>\d+)/$', RegistroUpdate.as_view(), name='registro_editar'),
    url(r'^eliminar_registro/(?P<pk>\d+)/$', RegistroDelete.as_view(), name='registro_eliminar'),

    url(r'^reportes_registro$', RegistroReport.as_view(), name='registro_reportes'),

    url(r'^api$', UserApi.as_view(), name='api'),

]