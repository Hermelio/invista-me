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

    # autor_livro = models.TextField(max_length=255)
    # ano_do_livro = models.DateField(default=datetime.now())
# class Usuario(models.Model):

#   nome = models.CharField(
#     max_length=255,
#     null=False,
#     blank=False
#   )

#   sobrenome = models.CharField(
#     max_length=255,
#     null=False,
#     blank=False
#   )

#   cpf = models.CharField(
#     max_length=14,
#     null=False,
#     blank=False
#   )

#   senha = models.IntegerField(
#     default=12,
#     null=False,
#     blank=False
#   )
