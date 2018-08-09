# Generated by Django 2.0.7 on 2018-08-08 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accesos', '0003_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuraciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segundosmensaje', models.PositiveIntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.Hotel')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.AccesosHotel')),
            ],
        ),
    ]