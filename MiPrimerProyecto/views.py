from html.entities import html5
from django.http import HttpResponse
import datetime

def mi_primera_vista(request):
    pass

    return HttpResponse("Saludos desde django en coder")

def segunda_vista(request):
    pass

    return HttpResponse("Buenas buenas!!")

def tiempo(request,name):
    hoy= datetime.datetime.now()
    nombre= name
    
    html= f"""
    <html>
    <body>
    <h1>El tiempo es : {hoy}</h1>
    <p>Hola soy {nombre}</p>
    </body>
    </html>
    """

    return HttpResponse(html)