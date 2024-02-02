# models.py
from django.db import models

class Pasta(models.Model):
    caminho = models.CharField(max_length=255)

