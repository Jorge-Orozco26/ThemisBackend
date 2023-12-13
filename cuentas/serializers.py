

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'rol', 'first_name', 'last_name', 'Departamento', 'Municipio', 'CarneAbogado', 'Biografia', 'Especialdad', 'Telefono', 'Cedula', 'Honorarios']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data): #crea una nueva instancia de CustomUser a partir de los datos validados
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            rol=validated_data['rol'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            Departamento=validated_data['Departamento'],
            Municipio=validated_data['Municipio'],
            CarneAbogado=validated_data.get('CarneAbogado', None),
            Biografia=validated_data.get('Biografia', None),
            Especialdad=validated_data.get('Especialidad', None),
            Telefono=validated_data['Telefono'],
            Cedula=validated_data['Cedula'],
            Honorarios=validated_data.get('Honorarios', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user