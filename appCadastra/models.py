from email.policy import default
from django.db import models
from django.utils import timezone

class CadastroOp(models.Model):
    numero_op               = models.CharField(max_length=20,blank=True)# Limitendo a quantidade de caracteres
    fornecedor              = models.CharField(max_length=20,blank=True)
    largura_capa            = models.CharField(max_length=20,blank=True)#FloatField
    comprimento_capa        = models.CharField(max_length=20,blank=True)
    expessura_capa          = models.CharField(max_length=20,blank=True)
    qualidade_capa          = models.CharField(max_length=20,blank=True)
    quantidade_producao     = models.CharField(max_length=20,blank=True)    
    hora_inicio_prod        = models.CharField(max_length=20,blank=True)# no cadastro incuir null
    hora_fim_prod           = models.CharField(max_length=20,blank=True)
    prod_atual              = models.CharField(max_length=20,blank=True)
    status                  = models.CharField(max_length=20,blank=True)
    