# Generated by Django 3.2.12 on 2022-03-18 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(db_column='description', max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, db_column='nombre', max_length=100, null=True),
        ),
    ]