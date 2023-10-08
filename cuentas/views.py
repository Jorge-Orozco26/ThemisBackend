from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from .models import CustomUser

#REGISTRO DE USUARIOS
@api_view(['POST']) #esta vista se utiliza para procesar solicitudes de registro de usuarios.
def register_user(request):
    if request.method == 'POST': #solo responde a POST
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(): #Verifica los datos de serializers
            serializer.save() #guarda
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#INICIO DE SESION CON TOKEN DE AUTENTICACION

@api_view(['POST']) #esta vista se utiliza para procesar solicitudes de inicio de sesion
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None #para inicio de sesion con correo electronico
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username) #si pone @ en username buscará en la BD si existe un email que coincida
            except ObjectDoesNotExist:                        #si se encuentra un usuario se asigna a la variable user
                pass

        if not user: #si no se encontró un usuario mediante la busqueda de email o si el valor de username no contiene un @
            user = authenticate(username=username, password=password) #se intenta autenticar al usuario utilizando los datos proporcionados

        if user:
            token, _ = Token.objects.get_or_create(user=user) #se genera un token de autenticación si el usuario se logra autenticar
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED) #manda error si no se autentica


@api_view(['POST'])
@permission_classes([IsAuthenticated]) #viste solo para usuarios autenticados
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete() #elimina el token de autenticacion 
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)