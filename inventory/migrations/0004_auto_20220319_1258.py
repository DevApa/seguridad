# Generated by Django 3.2.12 on 2022-03-19 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20220319_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headingdetail',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='headingdetail',
            name='user_create',
        ),
        migrations.RemoveField(
            model_name='headingdetail',
            name='user_update',
        ),
    ]
