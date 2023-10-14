from django.http.response import JsonResponse
from django.views import View
from .models import Ley

class LeyesView(View):
    
    def get(self, request):
        leyes= list(Leyes.object.values()) #listar las leyes
        if len(leyes)> 0:
            datos = {'message': "Transacción exitosa", 'leyes': leyes }
        else:
            datos = {'message': "No hay leyes..."}
        return JsonResponse(datos) #devuelve una lista JSON aunque no halla datos


    def post(self, request):
        datos = {'message' : "Transacción exitosa"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass