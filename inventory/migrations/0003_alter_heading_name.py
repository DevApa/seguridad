# Generated by Django 3.2.12 on 2022-03-18 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220317_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading',
            name='name',
            field=models.TextField(blank=True, db_column='nombre', max_length=100, null=True),
        ),
    ]
