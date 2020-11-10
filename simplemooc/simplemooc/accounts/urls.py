from django.conf.urls import url, include
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('entrar/', include('django.contrib.auth.urls')),
    # path('sair/', '', name="logout"),
    path('cadastre-se/', register, name="register"),
    path('editar/', edit, name="edit"),
    path('editar-senha/', edit_password, name="edit_password"),
]
