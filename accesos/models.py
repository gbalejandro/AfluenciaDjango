from django.db import models
from datetime import date
from django.contrib.auth.models import User


TIPOREGISTRO = [(1,'Entrada'),(2,'Salida')]


class Empleado(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=70)

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


class Tarjeta(models.Model):
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    tarjeta = models.CharField(max_length=15,unique=True)
    fcreacion = models.DateField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    fanulacion = models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.activa == False:
            self.fanulacion = date.today()

        super(Tarjeta, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {} - {}'.format(self.tarjeta,self.empleado.nombre + ' ' +self.empleado.apellidos, self.activa)


class Hotel(models.Model):
    hotelid = models.PositiveIntegerField(primary_key=True,verbose_name='Hotel ID')
    siglas = models.CharField(max_length=5,default='',blank=True,null=True)
    #complejo = models.ForeignKey(Complejo,on_delete=models.DO_NOTHING,blank=True,null=True)
    descripcion = models.CharField(max_length=50,verbose_name='Descripcion')

    def __str__(self):
        return '{} - {}'.format(self.hotelid,self.descripcion)
    
    
class Mensaje(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fechainicio =  models.DateField()
    fechafin = models.DateField()
    texto = models.CharField(max_length=250)
    #color = models.CharField(max_length=10,choices=COLORESMENSAJE,default='primary')
    visualizacion = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} - {} '.format(self.empleado.nombre + ' ' +self.empleado.apellidos, self.texto)


class AccesosHotel(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=25, unique=True)
    #accesopadre = models.ForeignKey('AccesosHotel', on_delete=models.PROTECT, blank=True, null=True)
    acceso = models.CharField(max_length=5)
    entradasalida = models.BooleanField(default=True,verbose_name='¿Contorlar entrada y salida?')

    def __str__(self):
        return '{} - {}'.format(self.hotel.descripcion, self.descripcion)


class Registro(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    zona = models.ForeignKey(AccesosHotel,on_delete=models.CASCADE)
    tipo = models.PositiveIntegerField(choices=TIPOREGISTRO)

    def save(self, *args, **kwargs):
        super(Registro, self).save(*args, **kwargs)


class Configuraciones(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    zona = models.ForeignKey(AccesosHotel,on_delete=models.CASCADE)
    segundosmensaje = models.PositiveIntegerField(verbose_name='Segundos Mensaje') 

    def __str__(self):
        return '{} - {}'.format(self.hotel.descripcion, self.zona)

