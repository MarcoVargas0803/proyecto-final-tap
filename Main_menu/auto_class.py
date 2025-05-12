from costos import CostosCorrectivos as Cost_corr
from costos import CostosPreventivos as Cost_prev


# Clase Auto
class Auto:
    def __init__(self, propietario=None, marca=None, modelo=None, anio=None, costo_total=0, tipo_mantenimiento="", id=None):
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
                self.costo_total += Cost_prev.llantas_con_desgaste(kilometraje)
            elif opcion == "2":
                self.costo_total += Cost_prev.cambio_aceite(kilometraje)
            elif opcion == "3":
                self.costo_total += Cost_prev.aceite_transmision(kilometraje)
            elif opcion == "4":
                self.costo_total += Cost_prev.amortiguadores(kilometraje)
            elif opcion == "5":
                self.costo_total += Cost_prev.caja_estandar(kilometraje)
            elif opcion == "6":
                self.costo_total += Cost_prev.caja_automatica(kilometraje)
            elif opcion == "7":
                self.costo_total += Cost_prev.sensores_luz(kilometraje)
            elif opcion == "8":
                self.costo_total += Cost_prev.refrigerante(kilometraje)
            else:
                print(f"Opción no válida: {opcion}")

    def realizar_mantenimiento_correctivo(self, kilometraje, opciones):
        self.tipo_mantenimiento = "correctivo"
        for opcion in opciones:
            if opcion == "1":
                self.costo_total += Cost_corr.desvielado(kilometraje)
            elif opcion == "2":
                self.costo_total += Cost_corr.caja_automatica(kilometraje)
            elif opcion == "3":
                self.costo_total += Cost_corr.caja_manual(kilometraje)
            elif opcion == "4":
                self.costo_total += Cost_corr.motor(kilometraje)
            elif opcion == "5":
                self.costo_total += Cost_corr.llanta_ponchada(kilometraje)
            elif opcion == "6":
                self.costo_total += Cost_corr.fallas_filtros(kilometraje)
            elif opcion == "7":
                self.costo_total += Cost_corr.fallas_bateria(kilometraje)
            else:
                print(f"Opción no válida: {opcion}")

    def info_basica(self):
        return f"{self.marca} {self.modelo} ({self.anio})"

    # ?  Pendiente de explicación de esta parte del codigo.
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Auto(**data)
