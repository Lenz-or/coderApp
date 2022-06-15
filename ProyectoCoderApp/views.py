import datetime
from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template,Context

# Create your views here.


def inicio(request):
    nombre= "Enzo"
    hoy= datetime.datetime.now()
    notas= [3,10,6,7,8,4]
    """with open(r"index.html") as file:
        plantilla = Template(file.read())

    contexto = Context({"mi_nombre": nombre, "dia_hora": hoy, "notas": notas})
"""
    return render(request, "index.html", {"mi_nombre": nombre, "dia_hora": hoy, "notas": notas})


def crear_curso(request):

    nombre= "python"
    comision = 31080

    nuevo_curso = Curso(nombre= nombre, comision= comision)
    nuevo_curso.save()

    return HttpResponse(f"Hemos agregado el curso de {nombre} con comision de {comision}")