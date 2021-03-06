# Generated by Django 2.0.7 on 2018-08-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accesos', '0004_configuraciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='empleados'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='color',
            field=models.CharField(default='primary', max_length=10),
        ),
        migrations.AlterField(
            model_name='configuraciones',
            name='segundosmensaje',
            field=models.PositiveIntegerField(default=3, verbose_name='Segundos Mensaje'),
        ),
    ]
