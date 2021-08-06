from django.db import models
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder


class Investimento(models.Model):  # tenho que usar o model para usar o banco de dados
    investimento = models.TextField(max_length=15)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now())
    perdido = models.BooleanField(default=False)

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
