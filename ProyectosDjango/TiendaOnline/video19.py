from gestionPedidos.models import Pedidos

Pedidos.objects.create(
    numero=1005,
    fecha='2019-12-30',
    entregado=True
    )

Pedidos.objects.create(
    numero=1006,
    fecha='2019-11-15',
    entregado=False
    )

Pedidos.objects.create(
    numero=1007,
    fecha='2019-11-19',
    entregado=True
    )

Pedidos.objects.create(
    numero=1008,
    fecha='2019-09-15',
    entregado=True
    )
