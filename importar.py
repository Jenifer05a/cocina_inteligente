import sqlite3
import csv

conexion = sqlite3.connect("db.sqlite3")

cursor = conexion.cursor()


with open('clientes_normalizado.csv', newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector)
    for fila in lector:
        cursor.execute(
            '''INSERT INTO cocina_inteligente_cliente(id, nombre_cliente, apellido_cliente)
            VALUES (?, ?, ?)''',
            fila)
print("CLIENTES IMPORTADOS")


with open('mesas_normalizado.csv', newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector)
    for fila in lector:
        cursor.execute(
            '''INSERT INTO cocina_inteligente_mesa(id, numero_mesa, capacidad)
            VALUES (?, ?, ?)''',fila)
        print("MESAS IMPORTADAS")


with open('reservaciones_normalizado.csv', newline='', encoding='utf-8') as archivo:

    lector = csv.reader(archivo)

    next(lector)

    for fila in lector:

        cursor.execute(

            '''
            INSERT INTO cocina_inteligente_reservacion
            (
                cliente_id,
                mesa_id,
                fecha,
                hora_inicio,
                hora_fin,
                numero_personas,
                estado
            )

            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',

            fila

        )

print("RESERVACIONES IMPORTADAS")


# ==========================================
# IMPORTAR RESEÑAS
# ==========================================

with open('resenas_normalizado.csv', newline='', encoding='utf-8') as archivo:

    lector = csv.reader(archivo)

    next(lector)

    for fila in lector:

        cursor.execute(

            '''
            INSERT INTO cocina_inteligente_resena
            (
                cliente_id,
                calificacion
            )

            VALUES (?, ?)
            ''',

            fila

        )

print("RESEÑAS IMPORTADAS")


# ==========================================
# GUARDAR CAMBIOS
# ==========================================

conexion.commit()


# ==========================================
# CERRAR CONEXION
# ==========================================

conexion.close()


print("\nDATOS IMPORTADOS CORRECTAMENTE")