from django.db import models

# Create your models here.
class Ley(models.Model): #creamos el modelo de base de datos para las leyes
    numero_de_ley = models.TextField()
    titulo = models.CharField(max_length=100)
    capitulo = models.CharField(max_length=100)
    articulo = models.CharField(max_length=50)
    descripcion_Ext = models.TextField()
    descripcion = models.TextField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)