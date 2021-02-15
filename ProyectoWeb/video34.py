# pendiente crear un servicio desde consola
from servicios.models import Servicio
from django.core.files.images import ImageFile


#crear usuario

"""
significado de "rb":
r es de read, el archivo es cargado como solo lectura
b es de binary, el archivo es cargado como binario, las imagenes son archivos binarios
"""

servicio=Servicio(
    imagen=ImageFile(open("descarga.jpg", "rb")),
    titulo='titulo',
    contenido='contenido'
)

servicio.save()

##################################

#eliminar usuario
#Servicio.objects.filter(titulo='titulo').delete()