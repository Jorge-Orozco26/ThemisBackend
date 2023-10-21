from django.db import models
from cuentas.models import CustomUser

# Create your models here.
class Ley(models.Model): #creamos el modelo de base de datos para las leyes
    numero_de_ley = models.CharField(max_length=50)
    titulo = models.CharField(max_length=255)
    capitulo = models.CharField(max_length=100)
    articulo = models.CharField(max_length=50)
    descripcion_Ext = models.TextField()
    descripcion = models.TextField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

