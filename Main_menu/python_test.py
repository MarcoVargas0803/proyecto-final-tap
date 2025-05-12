import bd_management
lista_nueva = bd_management.obtener_autos()

for auto in lista_nueva:
    print(f"auto: {auto.propietario}, {auto.marca}, {auto.modelo}, {auto.anio}, {auto.costo_total}, {auto.tipo_mantenimiento}")