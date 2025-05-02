import costos_preventivos as cost_prev
import costos_correctivos as cost_corr



# Clase Auto
class Auto:
    def __init__(self, propietario, marca, modelo, anio, costo_total=0, tipo_mantenimiento="", id=None):
        self.placa = id
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
                self.costo_total += cost_prev.llantas_con_desgaste(kilometraje)
            elif opcion == "2":
                self.costo_total += cost_prev.cambio_aceite(kilometraje)
            elif opcion == "3":
                self.costo_total += cost_prev.aceite_transmision(kilometraje)
            elif opcion == "4":
                self.costo_total += cost_prev.amortiguadores(kilometraje)
            elif opcion == "5":
                self.costo_total += cost_prev.caja_estandar(kilometraje)
            elif opcion == "6":
                self.costo_total += cost_prev.caja_automatica(kilometraje)
            elif opcion == "7":
                self.costo_total += cost_prev.sensores_luz(kilometraje)
            elif opcion == "8":
                self.costo_total += cost_prev.refrigerante(kilometraje)
            else:
                print(f"Opción no válida: {opcion}")

    def realizar_mantenimiento_correctivo(self, kilometraje, opciones):
        self.tipo_mantenimiento = "correctivo"
        for opcion in opciones:
            if opcion == "1":
                self.costo_total += cost_corr.desvielado(kilometraje)
            elif opcion == "2":
                self.costo_total += cost_corr.caja_automatica(kilometraje)
            elif opcion == "3":
                self.costo_total += cost_corr.caja_manual(kilometraje)
            elif opcion == "4":
                self.costo_total += cost_corr.motor(kilometraje)
            elif opcion == "5":
                self.costo_total += cost_corr.llanta_ponchada(kilometraje)
            elif opcion == "6":
                self.costo_total += cost_corr.fallas_filtros(kilometraje)
            elif opcion == "7":
                self.costo_total += cost_corr.fallas_bateria(kilometraje)
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
