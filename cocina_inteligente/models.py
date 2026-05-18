from django.db import models

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente}"

class Mesa(models.Model):
    numero_mesa = models.IntegerField()
    capacidad = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.numero_mesa}"

class Reservacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    numero_personas = models.IntegerField()
    ESTADOS = [
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('no_show', 'No Show'),
    ]
    estado = models.CharField(max_length=30, choices=ESTADOS)

    def __str__(self):
        return f"{self.cliente} - Mesa {self.mesa.numero_mesa}"


class Resena(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    def __str__(self):
        return f"{self.cliente} - {self.calificacion}"


class Platillo(models.Model):
    nombre_platillo = models.CharField(max_length=100, verbose_name="Nombre Platillo")
    descripcion = models.TextField(blank=True, verbose_name="Descripcion")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    CATEGORIAS = [
        ('bebidas', 'Bebidas'),
        ('entrada', 'Entrada'),
        ('postre', 'Postre'),
        ('comida', 'Comida'),
        ('plato principal', 'Plato principal'),
        ('guarniciones', 'Guarniciones')

    ]
    categoria = models.CharField(max_length=30, choices=CATEGORIAS, verbose_name="Categoria")
    disponibilidad = models.BooleanField(default=False, verbose_name="Disponibilidad")
    imagen= models.ImageField(upload_to='platillos', verbose_name="Imagen", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_platillo, self.categoria, self.disponibilidad, self.precio}"