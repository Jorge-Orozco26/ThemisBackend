from django.db import models

# Create your models here.
class Ley(models.Model): #creamos el modelo de base de datos para las leyes
    titulo = models.CharField(max_length=100)
    numero_de_ley = models.CharField(max_length=20)
    descripcion = models.TextField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)