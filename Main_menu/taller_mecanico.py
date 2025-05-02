from Main_menu import bd_management as bd


def menu():
    bd.limpiar_pantalla()
    bd.crear_base_datos()
    if not bd.iniciar_sesion():
        return
    while True:
        print("\n--- Menú ---")
        print("1. Agregar auto")
        print("2. Realizar mantenimiento")
        print("3. Mostrar autos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            auto = bd.agregar_auto()
            bd.guardar_auto(auto)
        elif opcion == "2":
            autos = bd.obtener_autos()
            if not autos:
                print("No hay autos registrados.")
            else:
                for i, auto in enumerate(autos, 1):
                    print(f"{i}. {auto.info_basica()}")
                try:
                    seleccion = int(input("Seleccione el auto (número): "))
                    bd.realizar_mantenimiento(autos[seleccion - 1])
                except (ValueError, IndexError):
                    print("Selección inválida.")
        elif opcion == "3":
            bd.mostrar_autos()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
