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

    def get(self, request, id=0):
        if (id>0):
            leyes= list(Ley.objects.filter(id=id).values()) #listar las leyes por id
            if len(leyes)> 0:
                laws =leyes[0]
                datos = {'message': "Transacción exitosa", 'laws': laws }
            else:
                datos = {'message': "Transacción inválida..."}
            return JsonResponse(datos) #devuelve una lista JSON aunque no halla datos
        else:
            leyes = list(Ley.objects.values())
            if len(leyes)>0:
                datos = {'message': "Transacción exitosa", 'leyes': leyes }
            else:
                datos = {'message': "Transacción inválida..."}
            return JsonResponse(datos)
    
    def post(self, request):
        try:
            jd = json.loads(request.body)
            Ley.objects.create(
                numero_de_ley=jd['numero_de_ley'],
                titulo=jd['titulo'],    
                capitulo=jd['capitulo'],
                articulo=jd['articulo'],
                descripcion_Ext=jd['descripcion_Ext'],
                descripcion=jd['descripcion']
            )
            datos = {'message': "Transacción exitosa"}
            return JsonResponse(datos)
        except KeyError as e:
            # Manejar el caso en el que una clave está ausente en la solicitud POST
            datos = {'error': f'La clave {str(e)} no se encuentra en la solicitud POST.'}
            return JsonResponse(datos, status=400)

    def put(self, request, id):
        jd = json.loads(request.body)
        leyes = list(Ley.objects.filter(id=id).values())  # Listar las leyes por id
        if len(leyes) > 0:
            laws = Ley.objects.get(id=id)

            # Actualiza solo los campos proporcionados en la solicitud
            if 'numero_de_ley' in jd:
                laws.numero_de_ley = jd['numero_de_ley']
            if 'titulo' in jd:
                laws.titulo = jd['titulo']
            if 'capitulo' in jd:
                laws.capitulo = jd['capitulo']
            if 'articulo' in jd:
                laws.articulo = jd['articulo']          
            if 'descripcion_Ext' in jd:
                laws.descripcion_Ext = jd['descripcion_Ext']
            if 'descripcion' in jd:
                laws.descripcion = jd['descripcion']
            laws.save()
            datos = {'message': "Transacción exitosa"}
        else:
            datos = {'message': "Transacción inválida..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        leyes = list(Ley.objects.filter(id=id).values())
        if len(leyes) > 0:
            Ley.objects.filter(id=id).delete()
            datos = {'message': "Transacción exitosa"}

        else:
            datos = {'message': "Transacción inválida..."}
        return JsonResponse(datos)