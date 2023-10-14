from django.urls import path
from .views import LeyesView

urlpatterns=[
    path('leyes/', LeyesView.as_view(), name='leyes_list'),#Name es endpoint
    path('leyes/<int:id>', LeyesView.as_view(), name='leyes_process')#servirá para los metodos put y delete
]