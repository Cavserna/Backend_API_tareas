from django.db import models

# Create your models here.

class Tarea (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField( auto_now_add=True)
    