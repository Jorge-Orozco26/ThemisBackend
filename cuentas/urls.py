

from django.urls import path
from .views import register_user, user_login, user_logout, UsuariosView 

urlpatterns = [
    path('register/', register_user, name='register'), #endpoint: register
    path('login/', user_login, name='login'), #endpoint login
    path('logout/', user_logout, name='logout'), #end point logout
    path('usuarios/', UsuariosView.as_view(), name='usuarios'),
    path('usuarios/<int:id>', UsuariosView.as_view(), name='usuarios_process')
]