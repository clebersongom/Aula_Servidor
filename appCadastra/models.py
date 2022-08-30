from email.policy import default
from django.db import models
from django.utils import timezone

class CadastroOp(models.Model):
    numero_op               = models.CharField(max_length=20)# Limitendo a quantidade de caracteres
    fornecedor              = models.CharField(max_length=20)
    largura_capa            = models.FloatField()
    comprimento_capa        = models.FloatField()
    expessura_capa          = models.FloatField()
    qualidade_capa          = models.CharField(max_length=20)
    quantidade_producao     = models.IntegerField()
    prioridade              = models.CharField(max_length=20)
    hora_inicio_prod        = models.DateTimeField()# no cadastro incuir null
    hora_fim_prod           = models.DateTimeField()
    