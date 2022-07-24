from django.db import models

class Familia(models.Model):
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField()

# Create your models here.
