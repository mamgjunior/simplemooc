from django.conf.urls import url, include
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('entrar/', include('django.contrib.auth.urls')),
    # path('sair/', '', name="logout"),
    path('cadastre-se/', register, name="register"),
]
