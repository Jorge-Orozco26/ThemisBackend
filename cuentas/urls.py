

from django.urls import path
from .views import register_user, user_login, user_logout

urlpatterns = [
    path('register/', register_user, name='register'), #endpoint: register
    path('login/', user_login, name='login'), #endpoint login
    path('logout/', user_logout, name='logout'), #end point logout
]