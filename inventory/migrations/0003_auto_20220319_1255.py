# Generated by Django 3.2.12 on 2022-03-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220319_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemassignmentheader',
            name='date',
        ),
        migrations.RemoveField(
            model_name='itemassignmentheader',
            name='user_create',
        ),
        migrations.RemoveField(
            model_name='itemassignmentheader',
            name='user_update',
        ),
        migrations.AlterField(
            model_name='itemassignmentheader',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, db_column='fecha_asignacion'),
        ),
    ]
