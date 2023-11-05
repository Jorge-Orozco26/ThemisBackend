
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone  
from django.core.validators import MinValueValidator, MaxValueValidator


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
    Departamento = models.CharField(max_length=50, null=True)
    Municipio = models.CharField(max_length=50, null=True)
    CarneAbogado = models.CharField(max_length=50, null=True)
    Biografia = models.TextField(null=True)
    Especialdad = models.CharField(max_length=50, null=True)
    Puntuaciones = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True,
        default=1  # 0 establece su valor predeterminado
    )
    Picture = models.CharField(max_length=255, null=True)
    Telefono = models.CharField(max_length=8, null=True)
    Cedula = models.CharField(max_length=16, null=True)

    
    
    rol= models.ForeignKey(Rol, on_delete=models.CASCADE)


    def __str__(self):
        return self.username


