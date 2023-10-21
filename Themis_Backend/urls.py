
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cuentas.urls')),  
    path('api/', include('CRUDleyes.urls')), 
    path('api/', include('tramitesLeg.urls')),
]