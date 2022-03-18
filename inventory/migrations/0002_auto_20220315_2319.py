# Generated by Django 3.2.12 on 2022-03-16 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemassigmenthardwaredetail',
            options={},
        ),
        migrations.AlterField(
            model_name='itemassigmenthardwaredetail',
            name='item',
            field=models.ForeignKey(db_column='id_item', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.item'),
        ),
        migrations.AlterModelTable(
            name='itemassigmenthardwaredetail',
            table='inv_item_asignacion_hardware_detalle',
        ),
        migrations.AlterModelTable(
            name='itemassignsoftwaredetail',
            table='inv_item_asignacion_software_detalle',
        ),
    ]
