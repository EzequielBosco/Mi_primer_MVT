from django.shortcuts import render

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

