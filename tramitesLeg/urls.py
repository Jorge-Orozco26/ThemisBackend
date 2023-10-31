from django.urls import path, include
from rest_framework import routers
from tramitesLeg import views
from .views import procedimientolegal


urlpatterns = [
    path('procedimientolegal/', procedimientolegal.as_view(), name='procedimientolegal_list')
]