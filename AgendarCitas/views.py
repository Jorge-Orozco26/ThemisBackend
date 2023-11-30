from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import AgendarCita
import json 

class CitasView(View):

    @method_decorator(csrf_exempt) #el CSRF es una medida de seguridad que evita que las solicitudes maliciosas se realicen en nombre de un usuario autenticado
    def dispatch(self, request, *args, **kwargs): # 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if (id>0):
            citas = list(AgendarCita.objects.filter(id=id).values())
            if len(citas)>0:
                agendar = citas[0]
                datos =  {'message': "Transacción exitosa", 'agendar': agendar }
            else:
                datos = {'message': "Transacción inválida..."}
            return JsonResponse(datos)
        else:
            citas = list(AgendarCita.objects.values())
            if len(citas)>0:
                datos = {'message': "Transacción exitosa", 'citas': citas }
            else:
                datos = {'message': "Transacción inválida..."}
            return JsonResponse(datos)