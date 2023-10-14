from django.urls import path
from .views import LeyesView

urlpatterns=[
    path('leyes/', LeyesView.as_view(), name='leyes_list')#Name es endpoint
]