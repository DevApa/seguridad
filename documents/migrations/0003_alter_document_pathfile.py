# Generated by Django 3.2.12 on 2022-03-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20220316_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='pathFile',
            field=models.FileField(blank=True, db_column='ruta_archivo', max_length=10000, null=True, upload_to='files/documents'),
        ),
    ]
