from django.shortcuts import render
from rest_framework import viewsets
from django.views import View
from .models import Procedimientos_Legales
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
#CRUD MODELO Procedimientos_Legales

class procedimientolegal(View):
    
    @method_decorator(csrf_exempt) #el CSRF es una medida de seguridad que evita que las solicitudes maliciosas se realicen en nombre de un usuario autenticado
    def dispatch(self, request, *args, **kwargs): #
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            procedimientos= list(Procedimientos_Legales.objects.filter(id=id).values()) #listar los registros por id
            if len(procedimientos)> 0:
                Procedure =procedimientos[0]
                datos = {'message': "Transacción exitosa", 'Procedure': Procedure }
            else:
                datos = {'message': "Transacción inválida..."}
            return JsonResponse(datos) #devuelve una lista JSON aunque no halla datos
        else:
            procedimientos = list(Procedimientos_Legales.objects.values())
            if len(procedimientos)>0:
                datos = {'message': "Transacción exitosa", 'procedimientos': procedimientos }
            else:
                datos = {'message': "Transacción inválida..."}
            return JsonResponse(datos)



#EL METODO POST NO FUNCIONA PORQUE DEPENDE DE UN CLAVE: REGISTRO_USUARIO/FOREIGN_KEY
    def post(self,request):
        try:
            jd = json.loads(request.body)
            Procedimientos_Legales.objects.create(
                Nombre_Procedimiento=jd['Nombre_Procedimiento'],
                DescripcionProcedimiento=jd['DescripcionProcedimiento'],    
                PasosSeguir=jd['PasosSeguir'],
                Usuario_Registro=jd['Usuario_Registro'],
                Fecha_Registro=jd['Fecha_Registro'],
                Estado=jd['Estado']
            )
            datos = {'message': "Transacción exitosa"}
            return JsonResponse(datos)
        except KeyError as e:
            # Manejar el caso en el que una clave está ausente en la solicitud POST
            datos = {'error': f'La clave {str(e)} no se encuentra en la solicitud POST.'}
            return JsonResponse(datos, status=400)

    def put(self,request):
        pass
    def delete(self,request):
        pass
