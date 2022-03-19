from django.db import models

from authentication.models import Usuario
from organization.models import Department


class Frequency(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True,  db_column='nombre')
    description = models.CharField(max_length=100, unique=True, db_column='descripcion')
    user_create = models.CharField(max_length=25, null=True, db_column='usuario_registra')
    user_modify = models.CharField(max_length=25, null=True, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.description)

    class Meta:
        verbose_name = 'Frecuencia'
        db_table = 'inv_frecuencia'


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True, db_column='nombre')
    description = models.CharField(max_length=100, unique=True, db_column='descripcion')
    state = models.BooleanField(default=False, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.description)

    class Meta:
        db_table = 'inv_tecnologia'


class Brand(models.Model):
    code = models.TextField(db_column='codigo', null='True', max_length=1000, unique=True)
    name = models.TextField(max_length=100, unique=True, null='True', db_column='nombre')
    description = models.TextField(max_length=1000, unique=True, db_column='descripcion')
    user_create = models.CharField(max_length=25, null='True', db_column='usuario_registra')
    user_modify = models.CharField(max_length=25, null='True', db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Marca'
        db_table = 'inv_marca'


class EModel(models.Model):
    name = models.CharField(max_length=100, null=True, db_column='nombre')
    description = models.CharField(max_length=1000, null=False, blank=False, unique=True, db_column='Descripcion')
    user_create = models.CharField(max_length=25, null=True, db_column='usuario_registra')
    user_modify = models.CharField(max_length=25, null=True, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.description)

    class Meta:
        verbose_name = 'Modelo'
        db_table = 'inv_modelo'


class Location(models.Model):
    departament = models.ForeignKey(Department, db_column='id_departamento', on_delete=models.CASCADE)
    name = models.CharField(db_column='nombre', max_length=255)
    description = models.CharField(db_column='description', max_length=1000)
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_modify = models.CharField(max_length=25, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.description)

    class Meta:
        db_table = 'inv_ubicacion'


class Generation(models.Model):
    name = models.CharField(db_column='nombre', max_length=255)
    description = models.CharField(db_column='description', max_length=1000)
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_modify = models.CharField(max_length=25, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.description)

    class Meta:
        db_table = 'inv_generacion'


class Type(models.Model):
    code = models.CharField(db_column='codigo', max_length=5)
    description = models.CharField(db_column='description', max_length=1000)
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_update = models.CharField(max_length=25, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'inv_tipo'


class Item(models.Model):
    description = models.CharField(db_column='description', max_length=1000)
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_update = models.CharField(max_length=25, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'inv_item'


class Software(models.Model):
    code = models.TextField(db_column='codigo', null=True, max_length=6)
    description = models.TextField(db_column='description', max_length=1000)
    version = models.TextField(db_column='version', max_length=100)
    user_create = models.CharField(max_length=25, null='True', db_column='usuario_registra')
    user_update = models.CharField(max_length=25, null='True', db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'inv_software'


class Heading(models.Model):
    item = models.ForeignKey(Item, db_column='id_item', on_delete=models.CASCADE)
    code = models.TextField(db_column='codigo', max_length=9)
    description = models.TextField(db_column='description', max_length=1000)
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_update = models.CharField(max_length=25, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_updated = models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'inv_rubro'


class HeadingDetail(models.Model):
    heading = models.ForeignKey(Heading, db_column='codigo', on_delete=models.CASCADE, verbose_name="Rubro")
    description = models.CharField(db_column='description', max_length=1000)
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_update = models.CharField(max_length=25, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_updated = models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'inv_rubro_detalle'


class HeadingCapacity(models.Model):
    heading = models.ForeignKey(Heading, db_column='codigo', on_delete=models.CASCADE, verbose_name="Rubro")
    value = models.CharField(db_column='valor', max_length=1000, verbose_name="Descripcion")
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_update = models.CharField(max_length=25, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_updated = models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.value

    class Meta:
        db_table = 'inv_rubro_capacidad'


class ItemAssignmentHeader(models.Model):
    employee = models.ForeignKey(Usuario, db_column='empleado', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, db_column='ubicacion', on_delete=models.CASCADE)
    name_equipment = models.TextField(max_length=1000, db_column='nombre_equipo')
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_update = models.CharField(max_length=25, db_column='usuario_modifica')
    date = models.DateField(db_column='fecha', auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name_equipment

    class Meta:
        db_table = 'inv_item_asignacion_cabecera'


class SoftwareDetail(models.Model):
    head = models.ForeignKey(ItemAssignmentHeader, db_column='id_cab_asignacion', on_delete=models.CASCADE)
    software = models.ForeignKey(Software, db_column='id_software', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, db_column='id_tipo', on_delete=models.CASCADE)
    user_create = models.CharField(max_length=25, db_column='usuario_registra')
    user_update = models.CharField(max_length=25, db_column='usuario_modifica')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_updated = models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')
    state = models.BooleanField(default=True, db_column='estado')

    class Meta:
        db_table = 'inv_soft_asignacion_detalle'


class ItemAssigmentHardwareDetail(models.Model):
    head = models.ForeignKey(ItemAssignmentHeader, db_column='id_cabecera_asignacion', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, db_column='id_tipo', null=True, blank=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, db_column='id_item', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, db_column='id_marca', on_delete=models.CASCADE)
    model = models.ForeignKey(EModel, db_column='id_modelo',  null=True, blank=True, on_delete=models.CASCADE)
    heading = models.ForeignKey(Heading, db_column='id_rubro', on_delete=models.CASCADE)
    heading_detail = models.ForeignKey(HeadingDetail, db_column='id_rubro_detalle', on_delete=models.CASCADE)
    frequency = models.ForeignKey(Frequency, db_column='id_frecuencia',  null=True, blank=True, on_delete=models.CASCADE)
    heading_capacity = models.ForeignKey(HeadingCapacity, db_column='id_rubro_capacidad', on_delete=models.CASCADE)
    generation = models.ForeignKey(Generation, db_column='id_generacion',  null=True, blank=True, on_delete=models.CASCADE)
    code_inventory = models.TextField(max_length=25, db_column='codigo_inventario')
    num_serial = models.TextField(max_length=25, db_column='numero_serie')
    quantity = models.IntegerField(db_column='cantidad')
    observation = models.TextField(max_length=1000, null=True, blank=True, db_column='observacion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.head

    class Meta:
        verbose_name = 'inv_item_asignacion_hardware_detalle'
        db_table = 'inv_item_asignacion_hardware_detalle'
