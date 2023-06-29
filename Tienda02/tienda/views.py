from django.shortcuts import render

def index(request):
    return render(request, 'tienda/index.html')

# Agrega las funciones de vista para las otras URLs aquí
