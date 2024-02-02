# urls.py
from django.urls import path
from leitor_gia.views import minha_interface

urlpatterns = [
    path('', minha_interface, name='minha_interface'),
]
