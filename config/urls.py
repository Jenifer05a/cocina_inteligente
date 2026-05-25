from django.contrib import admin
from django.urls import path
from cocina_inteligente import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.inicio, name='inicio'),

    path('menu/', views.menu, name='menu'),

    path('horas_pico/', views.horas_pico, name='horas_pico'),

    path('reservaciones_dia/', views.reservaciones_por_dia, name='reservaciones_dia'),

    path('estado/', views.total_por_estado, name='estado'),

    path('clientes/', views.clientes_mas_reservaciones, name='clientes'),

    path('mesas/', views.mesas_mas_utilizadas, name='mesas'),

    path('promedio_personas/', views.promedio_personas, name='promedio_personas'),

    path('numero_personas/', views.reservaciones_numero_personas, name='numero_personas'),

    path('no_shows/', views.cantidad_no_shows, name='no_shows'),

    path('tiempo_promedio/',views.tiempo_promedio_estancia,name='tiempo_promedio'),

    path('fecha_estado/', views.reservaciones_fecha_estado, name='fecha_estado'),

    path('calificacion/', views.promedio_calificacion, name='calificacion'),

    path('platillos/',views.ver_platillos,name='platillos'),

    path('crear_platillo/',views.crear_platillo,name='crear_platillo'),

    path('detalle_platillo/<int:id>/',views.detalle_platillo,name='detalle_platillo'),

    path('editar_platillo/<int:id>/',views.editar_platillo,name='editar_platillo'),

    path('eliminar_platillo/<int:id>/',views.eliminar_platillo,name='eliminar_platillo'),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)