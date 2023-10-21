from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken



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
            except CustomUser.DoesNotExist:
                pass

        if user is None:
            user = authenticate(request, username=username, password=password) #se intenta autenticar al usuario utilizando los datos proporcionados

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

        return Response({'access_token': access_token}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated]) #vista solo para usuarios autenticados
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete() #elimina el token de autenticacion 
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)