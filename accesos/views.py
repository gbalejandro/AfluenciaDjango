from django.shortcuts import render
from .models import Hotel,Mensaje,AccesosHotel,Tarjeta,Empleado,Registro,Configuraciones
from django.contrib.auth.decorators import login_required
from datetime import date


def HotelesList(request):
    conf = Configuraciones.objects.first()
    if conf:
        c = AccesosHotel.objects.filter(hotel=conf.hotel_id)
        if c:
            request.session['nombreHotel'] = c[0].hotel.descripcion
        request.session['zonaid'] = conf.zona_id
        request.session['nombrezona'] = AccesosHotel.objects.get(pk=conf.zona_id).descripcion
        return render(request,'accesos/busca_empleado.html')
    else:
        hoteles = Hotel.objects.all()
        return render(request,'accesos/hoteles_list.html',context={'Hotel_list':hoteles})


def Zonaslist(request,hotelid):

    request.session['hotelid'] = hotelid

    c = AccesosHotel.objects.filter(hotel=hotelid)
    if c:
        request.session['nombreHotel'] = c[0].hotel.descripcion

    return render(request, 'accesos/zonas_list.html', context={'zonas': c})



def Teclado(request,zonaid):
    request.session['zonaid'] = zonaid
    request.session['nombrezona'] = AccesosHotel.objects.get(pk=zonaid).descripcion
    return render(request,'accesos/busca_empleado.html')


def Registra(request,empleadoid):
    print(empleadoid)
    t = Tarjeta.objects.filter(tarjeta = empleadoid)

    mensaje = []
    if t.exists():
        emp = t[0].empleado
        #if emp.accesos.filter(pk=request.session['zonaid']):
        hoy = date.today()
        z= AccesosHotel.objects.get(pk=request.session['zonaid'])
        tipo = 1
        if z.entradasalida:
            r = Registro.objects.filter(empleado=emp,zona_id=request.session['zonaid']).last()

            if r:
                if r.tipo == 1:
                    tipo = 2
                    mensaje.append(('Hasta pronto', 'success'))
                else:
                    tipo = 1
                    mensaje.append(('Bienvenido', 'success'))
            else:
                mensaje.append(('Bienvenido', 'success'))
        else:
            mensaje.append(('Bienvenido', 'success'))


        mensajes = Mensaje.objects.filter(empleado=emp,fechainicio__lte=hoy,fechafin__gte=hoy)
        for m in mensajes:
            mensaje.append((m.texto, m.color))
            m.visualizacion = m.visualizacion+1
            m.save()

        Registro(empleado=emp,zona_id=request.session['zonaid'],tipo=tipo).save()

        tiempo = Configuraciones.objects.first()

        return render(request,'accesos/registrado.html',context={'empleado':emp,'mensaje':mensaje,'tiempo':tiempo})
        #else:
            #return render(request,'accesos/noacceso.html')
    else:
        tiempo = Configuraciones.objects.first()

        return render(request,'accesos/noregistrado.html',context={'tiempo':tiempo})
