# Generated by Django 2.0.7 on 2018-08-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accesos', '0002_auto_20180808_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.PositiveIntegerField(choices=[(1, 'Entrada'), (2, 'Salida')])),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.Empleado')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.AccesosHotel')),
            ],
        ),
    ]