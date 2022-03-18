# Generated by Django 3.2.12 on 2022-03-18 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='nombre', max_length=100, unique=True)),
                ('description', models.TextField(db_column='descripcion', max_length=1000, unique=True)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'inv_marca',
            },
        ),
        migrations.CreateModel(
            name='EModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=100, unique=True)),
                ('description', models.CharField(db_column='Descripcion', max_length=1000, unique=True)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'verbose_name': 'Modelo',
                'db_table': 'inv_modelo',
            },
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=100, unique=True)),
                ('description', models.CharField(db_column='descripcion', max_length=100, unique=True)),
                ('state', models.BooleanField(db_column='estado', default=False)),
            ],
            options={
                'verbose_name': 'Frecuencia',
                'db_table': 'inv_frecuencia',
            },
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=255)),
                ('description', models.CharField(db_column='description', max_length=1000)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'inv_generacion',
            },
        ),
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='nombre', max_length=100)),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'inv_rubro',
            },
        ),
        migrations.CreateModel(
            name='HeadingCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(db_column='valor', max_length=1000, verbose_name='Descripcion')),
                ('user_create', models.CharField(db_column='usuario_registra', max_length=25)),
                ('user_update', models.CharField(db_column='usuario_modifica', max_length=25)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('date_updated', models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('heading', models.ForeignKey(db_column='codigo', on_delete=django.db.models.deletion.CASCADE, to='inventory.heading', verbose_name='Rubro')),
            ],
            options={
                'db_table': 'inv_rubro_capacidad',
            },
        ),
        migrations.CreateModel(
            name='HeadingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(db_column='description', max_length=1000)),
                ('user_create', models.CharField(db_column='usuario_registra', max_length=25)),
                ('user_update', models.CharField(db_column='usuario_modifica', max_length=25)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('date_updated', models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('heading', models.ForeignKey(db_column='codigo', on_delete=django.db.models.deletion.CASCADE, to='inventory.heading', verbose_name='Rubro')),
            ],
            options={
                'db_table': 'inv_rubro_detalle',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=100)),
                ('description', models.CharField(db_column='description', max_length=1000)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'inv_item',
            },
        ),
        migrations.CreateModel(
            name='ItemAssignmentHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_equipment', models.TextField(db_column='nombre_equipo', max_length=1000)),
                ('user_create', models.CharField(db_column='usuario_registra', max_length=25)),
                ('user_update', models.CharField(db_column='usuario_modifica', max_length=25)),
                ('date', models.DateField(db_column='fecha')),
                ('date_updated', models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('employee', models.ForeignKey(db_column='empleado', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'inv_item_asignacion_cabecera',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=255)),
                ('description', models.CharField(db_column='description', max_length=1000)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'inv_ubicacion',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='nombre', max_length=100)),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('version', models.TextField(db_column='version', max_length=100)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'inv_software',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=100)),
                ('description', models.CharField(db_column='description', max_length=1000)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'inv_tipo',
            },
        ),
        migrations.CreateModel(
            name='SoftwareDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_create', models.CharField(db_column='usuario_registra', max_length=25)),
                ('user_update', models.CharField(db_column='usuario_modifica', max_length=25)),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('date_updated', models.DateTimeField(auto_now_add=True, db_column='fecha_modificacion')),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('head', models.ForeignKey(db_column='id_cab_asignacion', on_delete=django.db.models.deletion.CASCADE, to='inventory.itemassignmentheader')),
                ('software', models.ForeignKey(db_column='id_software', on_delete=django.db.models.deletion.CASCADE, to='inventory.software')),
            ],
            options={
                'db_table': 'inv_soft_asignacion_detalle',
            },
        ),
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(db_column='description', max_length=1000)),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('item', models.ForeignKey(db_column='id_item', on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('model', models.ForeignKey(db_column='id_modelo', on_delete=django.db.models.deletion.CASCADE, to='inventory.emodel')),
            ],
            options={
                'db_table': 'inv_item_modelo',
            },
        ),
        migrations.CreateModel(
            name='ItemAssignSoftwareDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('head', models.ForeignKey(db_column='id_cab_asignacion', on_delete=django.db.models.deletion.CASCADE, to='inventory.itemassignmentheader')),
                ('software', models.ForeignKey(db_column='id_software', on_delete=django.db.models.deletion.CASCADE, to='inventory.software')),
                ('type', models.ForeignKey(db_column='id_tipo', on_delete=django.db.models.deletion.CASCADE, to='inventory.tipo')),
            ],
            options={
                'db_table': 'inv_item_asignacion_software_detalle',
            },
        ),
        migrations.AddField(
            model_name='itemassignmentheader',
            name='location',
            field=models.ForeignKey(db_column='ubicacion', on_delete=django.db.models.deletion.CASCADE, to='inventory.location'),
        ),
        migrations.CreateModel(
            name='ItemAssigmentHardwareDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_inventory', models.TextField(db_column='codigo_inventario', max_length=25)),
                ('num_serial', models.TextField(db_column='numero_serie', max_length=25)),
                ('quantity', models.IntegerField(db_column='cantidad', default=0)),
                ('observation', models.TextField(blank=True, db_column='observacion', max_length=1000, null=True)),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('brand', models.ForeignKey(db_column='id_marca', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.brand')),
                ('frequency', models.ForeignKey(db_column='id_frecuencia', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.frequency')),
                ('generation', models.ForeignKey(db_column='id_generacion', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.generation')),
                ('head', models.ForeignKey(db_column='id_cabecera_asignacion', on_delete=django.db.models.deletion.CASCADE, to='inventory.itemassignmentheader')),
                ('heading', models.ForeignKey(db_column='id_rubro', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.heading')),
                ('heading_capacity', models.ForeignKey(db_column='id_rubro_capacidad', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.headingcapacity')),
                ('heading_detail', models.ForeignKey(db_column='id_rubro_detalle', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.headingdetail')),
                ('item', models.ForeignKey(db_column='id_item', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.item')),
                ('model', models.ForeignKey(db_column='id_modelo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.emodel')),
                ('type', models.ForeignKey(db_column='id_tipo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.tipo')),
            ],
            options={
                'db_table': 'inv_item_asignacion_hardware_detalle',
            },
        ),
        migrations.AddField(
            model_name='heading',
            name='item',
            field=models.ForeignKey(db_column='id_item', on_delete=django.db.models.deletion.CASCADE, to='inventory.item'),
        ),
    ]
