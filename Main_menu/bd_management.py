import os
import re
import sqlite3
from Main_menu.auto_class import Auto
# Funciones para manejo de base de datos
def crear_base_datos():
    conn = sqlite3.connect("../taller_mecanico.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS autos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        propietario TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        anio INTEGER NOT NULL,
        costo_total REAL DEFAULT 0,
        tipo_mantenimiento TEXT DEFAULT ''
    )
    """)
    conn.commit()
    conn.close()


def guardar_auto(auto):
    conn = sqlite3.connect("../taller_mecanico.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO autos (propietario, marca, modelo, anio, costo_total, tipo_mantenimiento)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (auto.propietario, auto.marca, auto.modelo, auto.anio, auto.costo_total, auto.tipo_mantenimiento))

    conn.commit()
    conn.close()


def obtener_autos():
    conn = sqlite3.connect("../taller_mecanico.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autos")
    rows = cursor.fetchall()

    conn.close()
    return [Auto(id=row[0], propietario=row[1], marca=row[2], modelo=row[3], anio=row[4], costo_total=row[5],
                 tipo_mantenimiento=row[6]) for row in rows]


def actualizar_auto(auto):
    conn = sqlite3.connect("../taller_mecanico.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE autos SET costo_total = ?, tipo_mantenimiento = ? WHERE id = ?
    """, (auto.costo_total, auto.tipo_mantenimiento, auto.id))

    conn.commit()
    conn.close()


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def agregar_auto():
    propietario = input("Nombre del propietario: ")
    while not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", propietario):
        propietario = input("Nombre inválido. Intente de nuevo: ") #Invalida nombre con caracteres especiale

    marca = input("Marca del auto: ")
    while not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", marca):
        marca = input("Marca inválida. Intente de nuevo: ")

    modelo = input("Modelo del auto: ")
    while not re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]+$", modelo):
        modelo = input("Modelo inválido. Intente de nuevo: ")

    while True:
        try:
            anio = int(input("Año del auto: "))
            break
        except ValueError:
            print("Entrada inválida. Ingrese solo números.")

    return Auto(propietario=propietario, marca=marca, modelo=modelo, anio=anio)


def realizar_mantenimiento(auto):
    try:
        kilometraje = int(input("Ingrese el kilometraje actual: "))
    except ValueError:
        print("Kilometraje inválido.")
        return

    tipo = input("Tipo de mantenimiento (preventivo/correctivo): ").strip().lower()
    while tipo not in ["preventivo", "correctivo"]:
        tipo = input("Entrada inválida. Ingrese 'preventivo' o 'correctivo': ").strip().lower()

    if tipo == "preventivo":
        print("\nSeleccione las correcciones (separadas por coma):")
        print("1. Llantas con desgaste\n2. Cambio de aceite\n3. Aceite de Transmisión\n4. Amortiguadores")
        print("5. Caja de velocidad Estándar\n6. Caja de velocidad Automática\n7. Sensores de luz\n8. Refrigerante")
        entrada = input("Opciones: ")
        opciones = entrada.split(",")
        auto.realizar_mantenimiento_preventivo(kilometraje, opciones)
    else:
        print("\nSeleccione las correcciones (separadas por coma):")
        print("1. Desvielado\n2. Caja automática\n3. Caja manual\n4. Motor\n5. Llanta ponchada")
        print("6. Fallas de Filtros\n7. Fallas de Batería")
        entrada = input("Opciones: ")
        opciones = entrada.split(",")
        auto.realizar_mantenimiento_correctivo(kilometraje, opciones)

    print(f"\nEl costo total del mantenimiento es: {auto.costo_total:.2f} pesos")
    actualizar_auto(auto)


def mostrar_autos():
    autos = obtener_autos()
    if autos:
        for auto in autos:
            print(auto.info_basica())
    else:
        print("No hay autos registrados.")

