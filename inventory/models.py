from django.db import models

from authentication.models import Usuario


class Frequency(models.Model):
    name = models.CharField(max_length=100, unique=True, db_column='nombre')
    description = models.CharField(max_length=100, unique=True, db_column='descripcion')
    state = models.BooleanField(default=False, db_column='estado')

    def __str__(self):
        txt = "{0} "
        return txt.format('Frecuencia')

    class Meta:
        verbose_name = 'Frecuencia'
        db_table = 'inv_frecuencia'


class Brand(models.Model):
    name = models.TextField(max_length=100, unique=True, db_column='nombre')
    description = models.TextField(max_length=1000, unique=True, db_column='descripcion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_marca'


class EModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, db_column='nombre')
    description = models.CharField(max_length=1000, null=False, blank=False, unique=True, db_column='Descripcion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        verbose_name = 'Modelo'
        db_table = 'inv_modelo'


class Location(models.Model):
    name = models.CharField(db_column='nombre', max_length=255)
    description = models.CharField(db_column='description', max_length=1000)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        db_table = 'inv_ubicacion'


class Generation(models.Model):
    name = models.CharField(db_column='nombre', max_length=255)
    description = models.CharField(db_column='description', max_length=1000)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        db_table = 'inv_generacion'


class Tipo(models.Model):
    name = models.CharField(db_column='nombre', max_length=100)
    description = models.CharField(db_column='description', max_length=1000)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_tipo'


class Item(models.Model):
    name = models.CharField(db_column='nombre', max_length=100)
    description = models.CharField(db_column='description', max_length=1000)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_item'


class ItemModel(models.Model):
    item = models.ForeignKey(Item, db_column='id_item', on_delete=models.CASCADE)
    model = models.ForeignKey(EModel, db_column='id_modelo', on_delete=models.CASCADE)
    description = models.CharField(db_column='description', max_length=1000)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'inv_item_modelo'


class Software(models.Model):
    name = models.TextField(db_column='nombre', max_length=100)
    description = models.TextField(db_column='description', max_length=1000)
    version = models.TextField(db_column='version', max_length=100)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_software'


class Heading(models.Model):
    item = models.ForeignKey(Item, db_column='id_item', on_delete=models.CASCADE)
    name = models.TextField(db_column='nombre', max_length=100)
    description = models.TextField(db_column='description', max_length=1000)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_rubro'


class HeadingDetailTecnology(models.Model):
    heading = models.ForeignKey(Heading, db_column='codigo', on_delete=models.CASCADE)
    name = models.TextField(db_column='nombre', max_length=100)
    description = models.TextField(db_column='description', max_length=1000)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_rubro_detalle_tecnologia'


class HeadingFeatures(models.Model):
    heading = models.ForeignKey(Heading, db_column='codigo', on_delete=models.CASCADE)
    name = models.TextField(db_column='nombre', max_length=100)
    value = models.CharField(db_column='valor', max_length=1000)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.heading

    class Meta:
        db_table = 'inv_rubro_caracteristicas'


class ItemAssignmentHeader(models.Model):
    employee = models.ForeignKey(Usuario, db_column='empleado', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, db_column='ubicacion', on_delete=models.CASCADE)
    name_equipment = models.TextField(max_length=1000, db_column='nombre_equipo')
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')

    def __str__(self):
        return self.employee.nombres

    class Meta:
        db_table = 'inv_item_asignacion_cabecera'


class ItemAssignSoftwareDetail(models.Model):
    head = models.ForeignKey(ItemAssignmentHeader, db_column='id_cab_asignacion', on_delete=models.CASCADE)
    software = models.ForeignKey(Software, db_column='id_software', on_delete=models.CASCADE)
    type = models.ForeignKey(Tipo, db_column='id_tipo', on_delete=models.CASCADE)
    state = models.BooleanField(default=True, db_column='estado')

    class Meta:
        db_table = 'inv_item_asignacion_software_detalle'


class ItemAssigmentHardwareDetail(models.Model):
    head = models.ForeignKey(ItemAssignmentHeader, db_column='id_cabecera_asignacion', on_delete=models.CASCADE)
    type = models.ForeignKey(Tipo, db_column='id_tipo', null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, db_column='id_item', null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, db_column='id_marca', null=True, on_delete=models.SET_NULL)
    model = models.ForeignKey(EModel, db_column='id_modelo', null=True, on_delete=models.SET_NULL)
    heading = models.ForeignKey(Heading, db_column='id_rubro', null=True, on_delete=models.SET_NULL)
    frequency = models.ForeignKey(Frequency, db_column='id_frecuencia', null=True, on_delete=models.SET_NULL)
    generation = models.ForeignKey(Generation, db_column='id_generacion', null=True, on_delete=models.SET_NULL)
    code_inventory = models.TextField(max_length=25, db_column='codigo_inventario')
    num_serial = models.TextField(max_length=25, db_column='numero_serie')
    quantity = models.IntegerField(default=0, db_column='cantidad')
    observation = models.TextField(max_length=1000, db_column='observacion', null=True, blank=True)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.head

    class Meta:
        db_table = 'inv_item_asignacion_hardware_detalle'



