from django.db import models
from cuentas.models import CustomUser

class AgendarCita(models.Model):
    Fecha_Cita = models.DateTimeField()
    Nombre_Usuario_citado = models.CharField(max_length=255)
    Descripcion= models.TextField()
    Observacion = models.TextField()

    usuario_agenda = models.ForeignKey(CustomUser, on_delete=models.CASCADE)