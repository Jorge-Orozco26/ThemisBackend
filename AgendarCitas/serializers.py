from rest_framework import serializers
from .models import AgendarCita

class AgendarCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendarCita
        fields = ['id', 'Fecha_Cita', 'Nombre_Usuario_citado', 'Descripcion', 'Observacion']
