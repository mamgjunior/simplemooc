from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    # re_path('(?P<pk>[0-9]+)/', details, name="details"),
    re_path('(?P<slug>[\w_-]+)/', details, name="details"),
]

# Obs.: Estou usando o (re_path) pois atualmente não se utiliza mais espressões regulares, mas caso queiram usar basta
# utilizar o (re_path) que as expressões regulares funcionaram.
