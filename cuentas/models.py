
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  #hereda la clase de abstractUser de Django y la extiende   
    email = models.EmailField(unique=True)
    ID_Rol = models.IntegerField()
    Usuario_Registro = models.CharField(max_length=50)
    Fecha_Registro = models.DateTimeField()


    def __str__(self):
        return self.username

