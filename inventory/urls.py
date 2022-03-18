from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from inventory.views.frecuencia.views import *
from inventory.views.generacion.views import *
from inventory.views.item.views import *
from inventory.views.marca.views import *
from inventory.views.modelo.views import *
from inventory.views.subitem.views import *
from inventory.views.tipo.views import *
from inventory.views.ubicacion.views import *
from inventory.views.subitemdet.views import *
from inventory.views.subitemcap.views import *
from inventory.views.software.views import *
from inventory.views.asignacioncabecera.views import *
from inventory.views.asignaciondethw.views import *
from inventory.views.asignaciondetsw.views import *

urlpatterns = [
    url(r'^marca/lista', login_required(BrandListView.as_view()), name='list-brand'),
    url(r'^marca/crear', login_required(BrandCreateView.as_view()), name='create-brand'),
    url(r'^marca/editar/(?P<pk>\d+)/$', login_required(BrandUpdateView.as_view()), name='update-brand'),
    url(r'^marca/eliminar/(?P<pk>\d+)/$', login_required(BrandDeleteView.as_view()), name='delete-brand'),

    url(r'^tipo/lista', login_required(TypeListView.as_view()), name='list-type'),
    url(r'^tipo/crear', login_required(TypeCreateView.as_view()), name='create-type'),
    url(r'^tipo/editar/(?P<pk>\d+)/$', login_required(TypeUpdateView.as_view()), name='update-type'),
    url(r'^tipo/eliminar/(?P<pk>\d+)/$', login_required(TypeDeleteView.as_view()), name='delete-type'),

    url(r'^generacion/lista', login_required(GenerationListView.as_view()), name='list-generation'),
    url(r'^generacion/crear', login_required(GenerationCreateView.as_view()), name='create-generation'),
    url(r'^generacion/editar/(?P<pk>\d+)/$', login_required(GenerationUpdateView.as_view()), name='update-generation'),
    url(r'^generacion/eliminar/(?P<pk>\d+)/$', login_required(GenerationDeleteView.as_view()), name='delete-generation'),

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

    url(r'^rubro/lista', login_required(HeadingListView.as_view()), name='list-subitem'),
    url(r'^rubro/crear', login_required(HeadingCreateView.as_view()), name='create-subitem'),
    url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-subitem'),
    url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-subitem'),

    url(r'^rubro_detalle/lista', login_required(HeadingDetailListView.as_view()), name='list-subitem-det'),
    url(r'^rubro_detalle/crear', login_required(HeadingDetailCreateView.as_view()), name='create-subitem-det'),
    # url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-subitem'),
    # url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-subitem'),

    url(r'^rubro_capacidad/lista', login_required(HeadingCapacityListView.as_view()), name='list-subitem-cap'),
    url(r'^rubro_capacidad/crear', login_required(HeadingCapacityCreateView.as_view()), name='create-subitem-cap'),
    # url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-subitem'),
    # url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-subitem'),

    url(r'^asignacion_cabecera/lista', login_required(ItemAssignmentHeaderListView.as_view()), name='list-assignment-cap'),
    url(r'^asignacion_cabecera/crear', login_required(ItemAssignmentHeaderCreateView.as_view()), name='create-assignment-cap'),
    # url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-subitem'),
    # url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-subitem'),

    url(r'^asignacion_hardware/lista', login_required(ItemAssigmentHardwareDetailListView.as_view()), name='list-assignment-hw'),
    url(r'^asignacion_hardware/crear', login_required(ItemAssigmentHardwareDetailCreateView.as_view()), name='create-assignment-hw'),
    # url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-subitem'),
    # url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-subitem'),

    url(r'^asignacion_software/lista', login_required(SoftwareDetailListView.as_view()), name='list-assignment-sw'),
    url(r'^asignacion_software/crear', login_required(SoftwareDetailCreateView.as_view()), name='create-assignment-sw'),
    # url(r'^rubro/editar/(?P<pk>\d+)/$', login_required(HeadingUpdateView.as_view()), name='update-subitem'),
    # url(r'^rubro/eliminar/(?P<pk>\d+)/$', login_required(HeadingDeleteView.as_view()), name='delete-subitem'),


]

app_name = 'inv'


