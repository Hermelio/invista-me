from django.db import models
from datetime import datetime


class Investimento(models.Model):  # tenho que usar o model para usar o banco de dados
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now())
