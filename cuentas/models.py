
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  #hereda la clase de abstractUser de Django y la extiende   
    email = models.EmailField(unique=True)
    # Add custom fields here, if needed

    def __str__(self):
        return self.username

    ROLES = (               
        ('usuario_C', 'Usuario_C'),
        ('abogado', 'Abogado'),
        ('administrador', 'Administrador'),
    )
    rol = models.CharField(max_length=15, choices=ROLES, default='usuario_C') #agregamos el rol al modelo de usuario
