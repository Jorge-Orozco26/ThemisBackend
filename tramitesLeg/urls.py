from django.urls import path, include
from rest_framework import routers
from tramitesLeg import views
from .views import procedimientolegal
from .views import PlantillaSoli


urlpatterns = [
    path('procedimientolegal/', procedimientolegal.as_view(), name='procedimientolegal_list'),
    path('procedimientolegal/<int:id>', procedimientolegal.as_view(), name='procedimientolegal_process'),
    path('plantillasolicitud/', PlantillaSoli.as_view(), name='plantillasolicitud_list'),
    path('plantillasolicitud/<int:id>', PlantillaSoli.as_view(), name='plantillasolicitud_process')
]
