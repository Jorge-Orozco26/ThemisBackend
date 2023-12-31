
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cuentas.urls')),  
    path('api/', include('CRUDleyes.urls')), 
    path('api/', include('tramitesLeg.urls')),
    path('api/', include('AgendarCitas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)