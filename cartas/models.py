from django.db import models
from datetime import datetime

class Carta(models.Model):
    titulo = models.CharField(max_length=255)
    tema = models.CharField(max_length=200)
    remetente = models.CharField(max_length=200)
    destinatario = models.CharField(max_length=200)
    texto = models.TextField()
    data_carta = models.DateTimeField(default=datetime.now, blank=True)
