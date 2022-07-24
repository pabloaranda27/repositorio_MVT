from django.shortcuts import render
from familiares.models import Familia
from datetime import date

def reg_familiar(request):
    nuevo_registro=Familia.objects.create(nombre='Alejandra',apellido='Esteves',fecha_nacimiento=date(1956,8,5), edad=65)
    context={
        'nuevo_registro':nuevo_registro
    }
    return render(request, 'reg_familiar.html', context=context)

def lista_familia(request):
    personas=Familia.objects.all()
    context={
        'personas':personas
    }
    return render(request, 'lista_familia.html', context=context)


# Create your views here.
