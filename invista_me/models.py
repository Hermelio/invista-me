from django.db import models
#from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ...


class Investimento(models.Model):  # tenho que usar o model para usar o banco de dados
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    investimento = models.TextField(max_length=15)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True)
    modify = models.DateField(auto_now=True)
    perdido = models.BooleanField(default=False)

    def __str__(self):
        return (f'{self.investimento} - R$ {self.valor} User {self.usuario}')


class Questions(models.Model):
    nome_contato = models.TextField(max_length=45)
    contact_email = models.EmailField(max_length=60)
    question = models.CharField(max_length=600)
