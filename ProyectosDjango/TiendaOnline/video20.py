from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

from django.contrib.auth.models import Group

user = User.objects.get(username = 'juan2')
user.delete()

user = User.objects.create_user(
    username='sonia', 
    password='123456789',
    first_name='Sonia',
    last_name='martin',
    email='sonia@pildorasinformaticas.es'
    )

user.is_staff=True

user.user_permissions.set([
    Permission.objects.get(name='Can add clientes'),
    Permission.objects.get(name='Can change clientes'),
    Permission.objects.get(name='Can delete clientes')
    ])

user.save()

grupo=Group.objects.create(name='administradores standard')

grupo=Group.objects.create(name='Mod. clientes-pedidos')

grupo.permissions.set([
    Permission.objects.get(name='Can add clientes'),
    Permission.objects.get(name='Can change clientes'),
    Permission.objects.get(name='Can delete clientes'),
    Permission.objects.get(name='Can view clientes'),

    Permission.objects.get(name='Can add pedidos'),
    Permission.objects.get(name='Can change pedidos'),
    Permission.objects.get(name='Can delete pedidos'),
    Permission.objects.get(name='Can view pedidos')
    ])

grupo.save()

user = User.objects.get(username = 'sonia')
user.user_permissions.clear()
user.user_permissions.add(Permission.objects.get(name='Can add articulos'))

user.groups.add(Group.objects.get(name='Mod. clientes-pedidos'))

user.save()