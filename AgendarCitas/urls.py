from django.urls import path
from .views import CitasView

urlpatterns=[
    path('citas/', CitasView.as_view(), name='citas_list'),#Name es endpoint
    path('citas/<int:id>', CitasView.as_view(), name='citas_process')#servirá para los metodos put y delete
]