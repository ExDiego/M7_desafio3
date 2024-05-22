from .models import Vehiculo, Chofer, Registro_contabilidad

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo.objects.create(
        patente=patente,
        marca=marca,
        modelo=modelo,
        year=year
    )
    return vehiculo

def crear_chofer(rut, nombre, apellido,):
    chofer = Chofer.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido
    )
    return chofer

def crear_registro_contabilidad(fecha_compra, valor, vehiculo_patente):
    vehiculo = Vehiculo.objects.get(patente=vehiculo_patente)
    registro_contabilidad = Registro_contabilidad.objects.create(
        fecha_compra=fecha_compra,
        valor=valor,
        vehiculo_id=vehiculo
    )
    return registro_contabilidad

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()
    return f'Chofer con rut: {rut} Deshabilitado'

def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = False
    vehiculo.save()
    return f'Vehiculo con patente: {patente} Deshabilitado'


def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()
    return f'Chofer con rut: {rut} Habilitado' 

def habilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente) 
    vehiculo.activo = True
    vehiculo.save()
    return f'Vehiculo con patente: {patente} Habilitado'

def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    print(f'Patente: {vehiculo.patente} Marca: {vehiculo.marca} Modelo: {vehiculo.modelo} año: {vehiculo.year} activo: {vehiculo.activo}')

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    print(f'Rut: {chofer.rut} Nombre: {chofer.nombre} Apellido: {chofer.apellido} activo: {chofer.activo}')
    
def asignar_chofer_a_vehiculo(rut, patente):
    try:
        chofer = Chofer.objects.get(rut=rut)
        vehiculo = Vehiculo.objects.get(patente=patente)
        chofer.vehiculo_id = vehiculo
        chofer.save()
        return f'Chofer con rut: {rut} asignado al vehiculo con patente: {patente}'
    except Chofer.DoesNotExist:
        return f'No se encontró a Chofer con rut: {rut}'
    except Vehiculo.DoesNotExist:
        return f'No se encontró a Vehiculo con patente: {patente}'

def imprimir_datos_vehiculo(patente):
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
        print(f'Patente: {vehiculo.patente} Marca: {vehiculo.marca} Modelo: {vehiculo.modelo} año: {vehiculo.year} activo: {vehiculo.activo}') 

        try:
            chofer = Chofer.objects.get(vehiculo_id=patente)
            print(f'Chofer asignado - Rut: {chofer.rut} Nombre: {chofer.nombre} Apellido: {chofer.apellido} activo: {chofer.activo}')
        except Chofer.DoesNotExist:
            print(f'No hay chofer asignado al vehiculo con patente: {patente}')
    except Vehiculo.DoesNotExist:
        print(f'No se encontró a Vehiculo con patente: {patente}')

##para diferenciar las funciones "obtener_vehiculo" e "imprimir_datos_vehiculo",
## se agrego un try con la variable "chofer", para que, en caso de que exista un
## chofer asignado al vehiculo, se impriman, también, los datos del chofer asignado.