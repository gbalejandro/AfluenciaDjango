"""entradas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accesos import views

urlpatterns = [
    url(r'^$', views.HotelesList, name='index_af'),
    path('zona/<int:hotelid>', views.Zonaslist, name='listazonasaf'),
    path('hoteles/', views.HotelesList, name='listahotelesaf'),
    path('teclado/<int:zonaid>', views.Teclado, name='tecladoaf'),
    #path('empleado/<int:empleadoid>',views.BuscaEmpleado, name='empleadocc'),
    path('registro/<empleadoid>', views.Registra,name='registroaf'),
    path('admin/', admin.site.urls),
    #url(r'\^media/(?P<path>.\*)\$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),  
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += patterns('', 
#     	url(r'\^media/(?P<path>.\*)\$', 'django.views.static.serve', 
#     		{'document_root': settings.MEDIA_ROOT, }),
# )
