# Generated by Django 2.0.7 on 2018-08-08 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccesosHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=25, unique=True)),
                ('acceso', models.CharField(max_length=5)),
                ('entradasalida', models.BooleanField(default=True, verbose_name='¿Contorlar entrada y salida?')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotelid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Hotel ID')),
                ('siglas', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainicio', models.DateField()),
                ('fechafin', models.DateField()),
                ('texto', models.CharField(max_length=250)),
                ('visualizacion', models.PositiveIntegerField(default=0)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.Empleado')),
            ],
        ),
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
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarjeta', models.CharField(max_length=15, unique=True)),
                ('fcreacion', models.DateField(auto_now_add=True)),
                ('activa', models.BooleanField(default=True)),
                ('fanulacion', models.DateField(blank=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.Empleado')),
            ],
        ),
        migrations.AddField(
            model_name='accesoshotel',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.Hotel'),
        ),
    ]