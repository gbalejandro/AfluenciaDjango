# Generated by Django 2.0.7 on 2018-08-08 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accesos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='zona',
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]