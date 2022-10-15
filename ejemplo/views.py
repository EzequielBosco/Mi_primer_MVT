from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html", 
    {
        "nombre":"Ezequiel",
        "apellido":"Bosco",
        })

def index_1(request):
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5]}
    )

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def imc(request, peso, altura):
    peso_m = peso / 100
    altura_cm = altura / 100
    imc = peso_m / (altura_cm * altura_cm) 
    return render(request, "ejemplo/imc.html", {"peso_m":peso, "altura_cm":altura}, {"imc": imc})