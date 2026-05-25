from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Avg
from .models import Reservacion, Resena, Platillo
from datetime import datetime
from .forms import PlatilloForm
from django.contrib import messages


def menu(request):
    return render(request, 'menu.html')


# =========================
# 1 HORAS PICO
# =========================
def horas_pico(request):

    reservaciones = (
        Reservacion.objects
        .values('hora_inicio')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    return render(request, 'consultas.html', {
        'titulo': 'Horas Pico',
        'reservaciones': reservaciones
    })


# =========================
# 2 RESERVACIONES POR DIA
# =========================
def reservaciones_por_dia(request):

    reservaciones = (
        Reservacion.objects
        .values('fecha')
        .annotate(total=Count('id'))
        .order_by('fecha')
    )

    return render(request, 'consultas.html', {
        'titulo': 'Reservaciones por Día',
        'reservaciones': reservaciones
    })


# =========================
# 3 TOTAL POR ESTADO
# =========================
def total_por_estado(request):

    reservaciones = (
        Reservacion.objects
        .values('estado')
        .annotate(total=Count('id'))
    )

    return render(request, 'consultas.html', {
        'titulo': 'Reservaciones por Estado',
        'reservaciones': reservaciones
    })


# =========================
# 4 CLIENTES FRECUENTES
# =========================
def clientes_mas_reservaciones(request):

    reservaciones = (
        Reservacion.objects
        .values(
            'cliente__nombre_cliente',
            'cliente__apellido_cliente'
        )
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    return render(request, 'consultas.html', {
        'titulo': 'Clientes Frecuentes',
        'reservaciones': reservaciones
    })


# =========================
# 5 MESAS MAS UTILIZADAS
# =========================
def mesas_mas_utilizadas(request):

    reservaciones = (
        Reservacion.objects
        .values('mesa__numero_mesa')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    return render(request, 'consultas.html', {
        'titulo': 'Mesas Más Utilizadas',
        'reservaciones': reservaciones
    })


# =========================
# 6 PROMEDIO PERSONAS
# =========================
def promedio_personas(request):

    reservaciones = Reservacion.objects.aggregate(
        promedio=Avg('numero_personas')
    )

    return render(request, 'consultas.html', {
        'titulo': 'Promedio de Personas',
        'reservaciones': [reservaciones]
    })


# =========================
# 7 RESERVACIONES POR PERSONAS
# =========================
def reservaciones_numero_personas(request):

    reservaciones = (
        Reservacion.objects
        .values('numero_personas')
        .annotate(total=Count('id'))
        .order_by('numero_personas')
    )

    return render(request, 'consultas.html', {
        'titulo': 'Reservaciones por Número de Personas',
        'reservaciones': reservaciones
    })


# =========================
# 8 NO SHOWS
# =========================
def cantidad_no_shows(request):

    total = Reservacion.objects.filter(
        estado='no_show'
    ).count()

    return render(request, 'consultas.html', {
        'titulo': 'Cantidad de No-Shows',
        'reservaciones': [{'no_shows': total}]
    })


# =========================
# 9 FECHA Y ESTADO
# =========================
def reservaciones_fecha_estado(request):

    reservaciones = (
        Reservacion.objects
        .values('fecha', 'estado')
        .annotate(total=Count('id'))
        .order_by('fecha')
    )

    return render(request, 'consultas.html', {
        'titulo': 'Reservaciones por Fecha y Estado',
        'reservaciones': reservaciones
    })


# =========================
# 10 PROMEDIO CALIFICACION
# =========================
def promedio_calificacion(request):

    promedio = Resena.objects.aggregate(
        promedio=Avg('calificacion')
    )

    return render(request, 'consultas.html', {
        'titulo': 'Promedio de Calificación',
        'reservaciones': [promedio]
    })


def tiempo_promedio_estancia(request):

    reservaciones = Reservacion.objects.all()

    total_minutos = 0

    cantidad = 0

    for r in reservaciones:

        inicio = datetime.strptime(

            str(r.hora_inicio),

            '%H:%M:%S'

        )

        fin = datetime.strptime(

            str(r.hora_fin),

            '%H:%M:%S'

        )

        diferencia = fin - inicio

        minutos = diferencia.seconds / 60

        total_minutos += minutos

        cantidad += 1

    if cantidad > 0:

        promedio = total_minutos / cantidad

    else:

        promedio = 0

    horas = int(promedio // 60)

    minutos = int(promedio % 60)

    tiempo_formateado = f"{horas}:{minutos:02d}"

    return render(

        request,

        'consultas.html',

        {

            'titulo': 'Tiempo Promedio de Estancia',

            'reservaciones': [

                {

                    'promedio_estancia': tiempo_formateado

                }

            ]

        }

    )


def tiempo_promedio_estancia(request):

    reservaciones = Reservacion.objects.all()

    total_minutos = 0

    cantidad = 0

    for r in reservaciones:

        inicio = datetime.strptime(

            str(r.hora_inicio),

            '%H:%M:%S'

        )

        fin = datetime.strptime(

            str(r.hora_fin),

            '%H:%M:%S'

        )

        diferencia = fin - inicio

        minutos = diferencia.seconds / 60

        total_minutos += minutos

        cantidad += 1

    if cantidad > 0:

        promedio = total_minutos / cantidad

    else:

        promedio = 0

    horas = int(promedio // 60)

    minutos = int(promedio % 60)

    tiempo_formateado = f"{horas}:{minutos:02d}"

    return render(

        request,

        'consultas.html',

        {

            'titulo': 'Tiempo Promedio de Estancia',

            'reservaciones': [

                {

                    'promedio_estancia': tiempo_formateado

                }

            ]

        }

    )

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from .models import Platillo

from .forms import PlatilloForm


# =========================
# LISTAR PLATILLOS
# =========================

def ver_platillos(request):

    platillos = Platillo.objects.all()

    return render(request, 'platillos.html', {

        'platillos': platillos

    })


# =========================
# CREAR PLATILLO
# =========================

def crear_platillo(request):

    if request.method == 'POST':

        formulario = PlatilloForm(

            request.POST,
            request.FILES

        )

        if formulario.is_valid():

            formulario.save()

            messages.success(

                request,

                '✅ Platillo agregado correctamente'

            )

            return redirect('platillos')

    else:

        formulario = PlatilloForm()

    return render(request, 'form_platillo.html', {

        'formulario': formulario,

        'modo_ver': False

    })


# =========================
# VER DETALLE
# =========================

def detalle_platillo(request, id):

    platillo = get_object_or_404(

        Platillo,

        pk=id

    )

    return render(request, 'form_platillo.html', {

        'platillo': platillo,

        'modo_ver': True

    })


# =========================
# EDITAR PLATILLO
# =========================

def editar_platillo(request, id):

    platillo = get_object_or_404(

        Platillo,

        pk=id

    )

    if request.method == 'POST':

        formulario = PlatilloForm(

            request.POST,
            request.FILES,
            instance=platillo

        )

        if formulario.is_valid():

            formulario.save()

            messages.success(

                request,

                '✏ Platillo editado correctamente'

            )

            return redirect('platillos')

    else:

        formulario = PlatilloForm(

            instance=platillo

        )

    return render(request, 'form_platillo.html', {

        'formulario': formulario,

        'platillo': platillo,

        'modo_ver': False

    })


# =========================
# ELIMINAR PLATILLO
# =========================

def eliminar_platillo(request, id):

    platillo = get_object_or_404(

        Platillo,

        pk=id

    )

    platillo.delete()

    messages.success(

        request,

        '🗑 Platillo eliminado correctamente'

    )

    return redirect('platillos')

def inicio(request):

    return render(request, 'inicio.html')