from django.http import HttpResponse
import datetime

def saludo(request): # primera vista

    documento="""<html>
    <body>
    <h1>
    Hola alumnos esta es nuestra primera página con Django
    </h1>
    </body>
    </html>"""

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego alumnos de Django")


def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):

    #edadActual=18
    periodo=agno-2019
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>""" %(agno, edadFutura)

    return HttpResponse(documento)