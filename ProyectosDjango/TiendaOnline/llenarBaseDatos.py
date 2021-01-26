from gestionPedidos.models import Clientes, Articulos

Clientes.objects.create(
    nombre='Juan', 
    direccion='Mi casa', 
    tfno='1234567')

Articulos.objects.create(
    nombre='mesa',
    seccion='decoracion',
    precio=90
    )

Articulos.objects.create(
    nombre='lampara',
    seccion='decoracion',
    precio=70
    )

Articulos.objects.create(
    nombre='pantalon',
    seccion='confeccion',
    precio=45
    )

Articulos.objects.create(
    nombre='destornillador',
    seccion='ferreteria',
    precio=35
    )

Articulos.objects.create(
    nombre='balon',
    seccion='deportes',
    precio=25
    )

Articulos.objects.create(
    nombre='raqueta',
    seccion='deportes',
    precio=105
    )

Articulos.objects.create(
    nombre='muneca',
    seccion='jugeteria',
    precio=15
    )

Articulos.objects.create(
    nombre='tren electrico',
    seccion='jugueteria',
    precio=135
    )