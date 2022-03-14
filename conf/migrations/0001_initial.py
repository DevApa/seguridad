# Generated by Django 3.2.12 on 2022-03-13 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'sec_icono',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=1000)),
                ('orden', models.IntegerField(default=0)),
                ('href', models.TextField(max_length=1000, null=True)),
                ('url', models.TextField(max_length=1000, null=True)),
                ('key', models.TextField(max_length=1000, null=True)),
                ('icon', models.ForeignKey(db_column='icono', on_delete=django.db.models.deletion.CASCADE, to='conf.icono')),
            ],
            options={
                'db_table': 'sec_menu',
                'ordering': ('orden',),
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'sec_rol',
            },
        ),
        migrations.CreateModel(
            name='RolMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=1000, null=True)),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='conf.menu')),
                ('rol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='conf.rol')),
            ],
            options={
                'db_table': 'sec_rol_menu',
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=1000)),
                ('orden', models.IntegerField(default=0)),
                ('key', models.TextField(max_length=1000)),
                ('icon', models.ForeignKey(db_column='icono', on_delete=django.db.models.deletion.CASCADE, to='conf.icono')),
            ],
            options={
                'db_table': 'sec_modulo',
                'ordering': ('orden',),
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='modulo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='conf.modulo'),
        ),
        migrations.AddField(
            model_name='menu',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='conf.menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='roles',
            field=models.ManyToManyField(through='conf.RolMenu', to='conf.Rol'),
        ),
    ]
