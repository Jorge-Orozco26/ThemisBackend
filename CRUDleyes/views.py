from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Ley
import json

class LeyesView(View):
    
    @method_decorator(csrf_exempt) #el CSRF es una medida de seguridad que evita que las solicitudes maliciosas se realicen en nombre de un usuario autenticado
    def dispatch(self, request, *args, **kwargs): #
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        leyes= list(Ley.objects.values()) #listar las leyes
        if len(leyes)> 0:
            datos = {'message': "Transacción exitosa", 'leyes': leyes }
        else:
            datos = {'message': "No hay leyes..."}
        return JsonResponse(datos) #devuelve una lista JSON aunque no halla datos


    def post(self, request):
        jd =json.loads(request.body)
        Ley.objects.create(titulo=jd['titulo'], numero_de_ley=jd['numero_de_ley'],descripcion=jd['descripcion'], articulo=jd['articulo'])
        datos = {'message' : "Transacción exitosa"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass