from django.urls import path
from .views import *

urlpatterns = [
    # path('entrar/', '', name="login"),
    path('cadastre-se/', register, name="register"),
]
