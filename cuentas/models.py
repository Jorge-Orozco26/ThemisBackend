
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone  # Asegúrate de importar timezone



class Rol(models.Model):
    ID_Rol = models.AutoField(primary_key=True)
    Codigo_Rol = models.CharField(max_length=50)
    Nombre_Rol = models.CharField(max_length=255)
    Usuario_Registro = models.CharField(max_length=50)
    Fecha_Registro = models.DateTimeField()
    estado = models.BooleanField()

    def __str__(self):
        return self.Nombre_Rol

class CustomUser(AbstractUser):  #hereda la clase de abstractUser de Django y la extiende   
    email = models.EmailField(unique=True)
    Usuario_Registro = models.CharField(max_length=50)
    Fecha_Registro = models.DateTimeField(default=timezone.now)
    
    rol= models.ForeignKey(Rol, on_delete=models.CASCADE)


    def __str__(self):
        return self.username


