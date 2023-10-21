from django.db import models
from cuentas.models import CustomUser


class Procedimientos_Legales(models.Model):
    ID_Procedimientos_Legales = models.AutoField(primary_key=True)# .AutoField Llave primaria/se incrementa
    Nombre_Procedimiento = models.CharField(max_length=255)#.Charfield para NVARCHAR
    DescripcionProcedimiento = models.TextField()
    PasosSeguir = models.TextField()
    Usuario_Registro = models.CharField(max_length=50)
    Fecha_Registro = models.DateTimeField()#.DateTimeField para fecha
    Estado = models.BooleanField()


    def __str__(self):
        return self.Nombre_Procedimiento

class Plantilla_Solicitud(models.Model):
    ID_Plantilla_Solicitud =models.AutoField(primary_key=True)
    Nombre = models.TextField()
    Contenido = models.TextField()
    ID_Procedimiento_Legales = models.IntegerField()
    Usuario_Registro = models.CharField(max_length=50)
    Fecha_Registro = models.DateTimeField()
    Estado = models.BooleanField()

    procedimiento_legales = models.ForeignKey(Procedimientos_Legales, on_delete=models.CASCADE)
    usuario_creador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class Solicitudes_Rellenas(models.Model):
    ID_Solicitudes_Rellenas = models.AutoField(primary_key=True)
    ID_Usuario = models.IntegerField()
    ID_Plantilla_Solicitud = models.IntegerField()
    Contenido_Rellenado = models.TextField()
    Usuario_Registro = models.CharField(max_length=50)
    Fecha_Registro = models.DateTimeField()
    Estado = models.BooleanField()

    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plantilla_solicitud = models.ForeignKey(Plantilla_Solicitud, on_delete=models.CASCADE)

    def __str__(self):
        return f"Solicitud Rellenada #{self.ID_Solicitudes_Rellenas}"

class Rol(models.Model):
    ID_Rol = models.AutoField(primary_key=True)
    Codigo_Rol = models.CharField(max_length=50)
    Nombre_Rol = models.CharField(max_length=255)
    Usuario_Registro = models.CharField(max_length=50)
    Fecha_Registro = models.DateTimeField()
    estado = models.BooleanField()

    def __str__(self):
        return self.Nombre_Rol





