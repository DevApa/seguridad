from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from inventory.views.asignacioncabecera.views import *
from inventory.views.asignaciondethw.views import *
from inventory.views.asignaciondetsw.views import *
from inventory.views.frecuencia.views import *
from inventory.views.generacion.views import *
from inventory.views.item.views import *
from inventory.views.marca.views import *
from inventory.views.modelo.views import *
from inventory.views.software.views import *
from inventory.views.subitem.views import *
from inventory.views.subitemcap.views import *
from inventory.views.subitemdet.views import *
from inventory.views.tipo.views import *
from inventory.views.ubicacion.views import *

app_name = 'inv'

urlpatterns = [
    url(r'^marca/lista', login_required(BrandListView.as_view()), name='list-brand'),
    url(r'^marca/crear', login_required(BrandCreateView.as_view()), name='create-brand'),
    url(r'^marca/editar/(?P<pk>\d+)/$', login_required(BrandUpdateView.as_view()), name='update-brand'),
    url(r'^marca/eliminar/(?P<pk>\d+)/$', login_required(BrandDeleteView.as_view()), name='delete-brand'),

    url(r'^tipo/lista', login_required(TypeListView.as_view()), name='list-type'),
    url(r'^tipo/crear', login_required(TypeCreateView.as_view()), name='create-type'),
    url(r'^tipo/editar/(?P<pk>\d+)/$', login_required(TypeUpdateView.as_view()), name='update-type'),
    url(r'^tipo/eliminar/(?P<pk>\d+)/$', login_required(TypeDeleteView.as_view()), name='delete-type'),

    url(r'^generacion/lista', login_required(GenerationList.as_view()), name='list-generation'),
    url(r'^generacion/crear', login_required(GenerationCreate.as_view()), name='create-generation'),
    url(r'^generacion/editar/(?P<pk>\d+)/$', login_required(GenerationUpdate.as_view()), name='update-generation'),
    url(r'^generacion/eliminar/(?P<pk>\d+)/$', login_required(GenerationDelete.as_view()), name='delete-generation'),

    url(r'^frecuencia/lista', login_required(FrequencyListView.as_view()), name='list-frequency'),
    url(r'^frecuencia/crear', login_required(FrequencyCreateView.as_view()), name='create-frequency'),
    url(r'^frecuencia/editar/(?P<pk>\d+)/$', login_required(FrequencyUpdateView.as_view()), name='update-frequency'),
    url(r'^frecuencia/eliminar/(?P<pk>\d+)/$', login_required(FrequencyDeleteView.as_view()), name='delete-frequency'),

    url(r'^ubicacion/lista', login_required(LocationListView.as_view()), name='list-location'),
    url(r'^ubicacion/crear', login_required(LocationCreateView.as_view()), name='create-location'),
    url(r'^ubicacion/editar/(?P<pk>\d+)/$', login_required(LocationUpdateView.as_view()), name='update-location'),
    url(r'^ubicacion/eliminar/(?P<pk>\d+)/$', login_required(LocationDeleteView.as_view()), name='delete-location'),

    url(r'^item/lista', login_required(ItemListView.as_view()), name='list-item'),
    url(r'^item/crear', login_required(ItemCreateView.as_view()), name='create-item'),
    url(r'^item/editar/(?P<pk>\d+)/$', login_required(ItemUpdateView.as_view()), name='update-item'),
    url(r'^item/eliminar/(?P<pk>\d+)/$', login_required(ItemDeleteView.as_view()), name='delete-item'),

    url(r'^modelo/lista', login_required(EModelListView.as_view()), name='list-model'),
    url(r'^modelo/crear', login_required(EModelCreateView.as_view()), name='create-model'),
    url(r'^modelo/editar/(?P<pk>\d+)/$', login_required(EModelUpdateView.as_view()), name='update-model'),
    url(r'^modelo/eliminar/(?P<pk>\d+)/$', login_required(EModelDeleteView.as_view()), name='delete-model'),

    url(r'^software/lista', login_required(SoftwareListView.as_view()), name='list-soft'),
    url(r'^software/crear', login_required(SoftwareCreateView.as_view()), name='create-soft'),
    url(r'^software/editar/(?P<pk>\d+)/$', login_required(SoftwareUpdateView.as_view()), name='update-soft'),
    url(r'^software/eliminar/(?P<pk>\d+)/$', login_required(SoftwareDeleteView.as_view()), name='delete-soft'),

    url(r'^rubro/lista', login_required(HeadingListView.as_view()), name='list-sub-item'),
    url(r'^rubro/crear', login_required(HeadingCreateView.as_view()), name='create-sub-item'),
    url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-sub-item'),
    url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-sub-item'),

    url(r'^rubro_detalle/lista', login_required(HeadingDetailListView.as_view()), name='list-sub-item-det'),
    url(r'^rubro_detalle/crear', login_required(HeadingDetailCreateView.as_view()), name='create-sub-item-det'),
    url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-sub-item-det'),
    url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-sub-item-det'),

    url(r'^rubro_capacidad/lista', login_required(HeadingCapacityListView.as_view()), name='list-sub-item-cap'),
    url(r'^rubro_capacidad/crear', login_required(HeadingCapacityCreateView.as_view()), name='create-sub-item-cap'),
    url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-sub-item-cap'),
    url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-sub-item-cap'),

    url(r'^asignar_cabecera/lista', login_required(IAHList.as_view()), name='list-assign-cap'),
    url(r'^asignar_cabecera/crear', login_required(IAHCreate.as_view()), name='create-assign-cap'),
    url(r'^asignar_cabecera/editar/(?P<pk>\d+)/$', login_required(IAHUpdate.as_view()), name='update-assign-cap'),
    url(r'^asignar_cabecera/eliminar/(?P<pk>\d+)/$', login_required(IAHDelete.as_view()), name='delete-assign-cap'),

    url(r'^asignar_hardware/lista', login_required(IAHDetail.as_view()), name='list-assign-hw'),
    url(r'^asignar_hardware/crear', login_required(IAHDetailCreate.as_view()), name='create-assign-hw'),
    url(r'^asignar_hardware/editar/(?P<pk>\d+)/$', login_required(IAHDetailUpdate.as_view()), name='update-assign-hw'),
    url(r'^asignar_hardware/eliminar/(?P<pk>\d+)/$', login_required(IAHDetailDelete.as_view()), name='del-assign-hw'),

    url(r'^asignar_software/lista', login_required(SoftDetList.as_view()), name='list-assign-sw'),
    url(r'^asignar_software/crear', login_required(SoftDetCreate.as_view()), name='create-assign-sw'),
    url(r'^asignar_software/editar/(?P<pk>\d+)/$', login_required(SoftDetUpdate.as_view()), name='update-assign-sw'),
    url(r'^asignar_software/eliminar/(?P<pk>\d+)/$', login_required(SoftDetDelete.as_view()), name='delete-assign-sw'),
]

