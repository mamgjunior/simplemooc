from distutils.command.config import config

from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contato/', contato, name="contato"),
]