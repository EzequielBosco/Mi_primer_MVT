from django.shortcuts import render
from blog.models import Configuracion

def index_0(request):
    configuracion = Configuracion.objects.first()
    return render(request, "blog/index.html", {"configuracion": configuracion})
