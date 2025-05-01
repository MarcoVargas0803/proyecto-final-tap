import os
import re
import sqlite3
from costos_preventivos import (
    llantas_con_desgaste, cambio_aceite, aceite_transmision,
    amortiguadores, caja_estandar, caja_automatica,
    sensores_luz, refrigerante
)
from costos_correctivos import (
    desvielado, caja_automatica as caja_auto_corr, caja_manual,
    motor, llanta_ponchada, fallas_filtros, fallas_bateria
)


# Clase Auto
class Auto:
    def __init__(self, propietario, marca, modelo, anio, costo_total=0, tipo_mantenimiento="", id=None,):
        self.id = id
        self.propietario = propietario
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.costo_total = costo_total
        self.tipo_mantenimiento = tipo_mantenimiento

    def realizar_mantenimiento_preventivo(self, kilometraje, opciones):
        self.tipo_mantenimiento = "preventivo"
        for opcion in opciones:
            if opcion == "1":
                self.costo_total += llantas_con_desgaste(kilometraje)
            elif opcion == "2":
                self.costo_total += cambio_aceite(kilometraje)
            elif opcion == "3":
                self.costo_total += aceite_transmision(kilometraje)
            elif opcion == "4":
                self.costo_total += amortiguadores(kilometraje)
            elif opcion == "5":
                self.costo_total += caja_estandar(kilometraje)
            elif opcion == "6":
                self.costo_total += caja_automatica(kilometraje)
            elif opcion == "7":
                self.costo_total += sensores_luz(kilometraje)
            elif opcion == "8":
                self.costo_total += refrigerante(kilometraje)
            else:
                print(f"Opción no válida: {opcion}")

    def realizar_mantenimiento_correctivo(self, kilometraje, opciones):
        self.tipo_mantenimiento = "correctivo"
        for opcion in opciones:
            if opcion == "1":
                self.costo_total += desvielado(kilometraje)
            elif opcion == "2":
                self.costo_total += caja_auto_corr(kilometraje)
            elif opcion == "3":
                self.costo_total += caja_manual(kilometraje)
            elif opcion == "4":
                self.costo_total += motor(kilometraje)
            elif opcion == "5":
                self.costo_total += llanta_ponchada(kilometraje)
            elif opcion == "6":
                self.costo_total += fallas_filtros(kilometraje)
            elif opcion == "7":
                self.costo_total += fallas_bateria(kilometraje)
            else:
                print(f"Opción no válida: {opcion}")

    def info_basica(self):
        return f"{self.marca} {self.modelo} ({self.anio})"

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Auto(**data)


# Funciones para manejo de base de datos
def crear_base_datos():
    conn = sqlite3.connect("taller_mecanico.db")
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
    conn = sqlite3.connect("taller_mecanico.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO autos (propietario, marca, modelo, anio, costo_total, tipo_mantenimiento)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (auto.propietario, auto.marca, auto.modelo, auto.anio, auto.costo_total, auto.tipo_mantenimiento))

    conn.commit()
    conn.close()


def obtener_autos():
    conn = sqlite3.connect("taller_mecanico.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autos")
    rows = cursor.fetchall()

    conn.close()
    return [Auto(id=row[0], propietario=row[1], marca=row[2], modelo=row[3], anio=row[4], costo_total=row[5],
                 tipo_mantenimiento=row[6]) for row in rows]


def actualizar_auto(auto):
    conn = sqlite3.connect("taller_mecanico.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE autos SET costo_total = ?, tipo_mantenimiento = ? WHERE id = ?
    """, (auto.costo_total, auto.tipo_mantenimiento, auto.id))

    conn.commit()
    conn.close()


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def iniciar_sesion():
    correo_valido = "alicia@gmail.com"
    contrasena_valida = "1234"
    while True:
        correo = input("Ingrese su correo electrónico: ")
        contrasena = input("Ingrese su contraseña: ")
        if correo == correo_valido and contrasena == contrasena_valida:
            print("Inicio de sesión exitoso.\n")
            return True
        else:
            print("Credenciales inválidas. Intente de nuevo.\n")


def agregar_auto():
    propietario = input("Nombre del propietario: ")
    while not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", propietario):
        propietario = input("Nombre inválido. Intente de nuevo: ")

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


def menu():
    limpiar_pantalla()
    crear_base_datos()
    if not iniciar_sesion():
        return
    while True:
        print("\n--- Menú ---")
        print("1. Agregar auto")
        print("2. Realizar mantenimiento")
        print("3. Mostrar autos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            auto = agregar_auto()
            guardar_auto(auto)
        elif opcion == "2":
            autos = obtener_autos()
            if not autos:
                print("No hay autos registrados.")
            else:
                for i, auto in enumerate(autos, 1):
                    print(f"{i}. {auto.info_basica()}")
                try:
                    seleccion = int(input("Seleccione el auto (número): "))
                    realizar_mantenimiento(autos[seleccion - 1])
                except (ValueError, IndexError):
                    print("Selección inválida.")
        elif opcion == "3":
            mostrar_autos()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
