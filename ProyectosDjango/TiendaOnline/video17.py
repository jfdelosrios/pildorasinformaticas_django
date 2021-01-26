from gestionPedidos.models import Clientes, Articulos

Clientes.objects.filter(nombre='Juan').delete()

Clientes.objects.create(
    nombre='Maria', 
    direccion='Gran Via', 
    email='maria@pildorasinformaticas.es',
    tfno='123456')

Clientes.objects.create(
    nombre='Elena', 
    direccion='P vergara', 
    tfno='1234')

t = Articulos.objects.get(
    nombre='tren electrico'
    )
t.precio = 250  # change field
t.save() # this will update only
