from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import AgendarCita
from .serializers import AgendarCitaSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.models import User

class CitasView(View):
    #@method_decorator(login_required, name='dispatch')
    @method_decorator(csrf_exempt) #el CSRF es una medida de seguridad que evita que las solicitudes maliciosas se realicen en nombre de un usuario autenticado
    def dispatch(self, request, *args, **kwargs): # 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            citas = list(AgendarCita.objects.filter(id=id).values())
            if len(citas) > 0:
                agendar = citas[0]
                datos = {'message': "Transacción exitosa", 'agendar': agendar}
            else:
                datos = {'message': "Transacción inválida..."}
            return JsonResponse(datos)
        else:
            citas = list(AgendarCita.objects.values())
            if len(citas) > 0:
                datos = {'message': "Transacción exitosa", 'citas': citas}
            else:
                datos = {'message': "Transacción inválida..."}
            return JsonResponse(datos)

    def post(self, request, *args, **kwargs):
        try:
            # Asegúrate de autenticar al usuario antes de intentar asignarlo
            if request.user.is_authenticated:
                data = json.loads(request.body)
                # Asigna la instancia de usuario autenticado a usuario_agenda
                data['usuario_agenda'] = request.user
                serializer = AgendarCitaSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'message': 'Transacción exitosa', 'id_cita': serializer.data['id']}, status=201)
                else:
                    return JsonResponse({'error': serializer.errors}, status=400)
            else:
                return JsonResponse({'error': 'Usuario no autenticado'}, status=401)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Error al decodificar JSON: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)