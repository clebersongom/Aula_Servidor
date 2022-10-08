from email.policy import default
from itertools import pairwise
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
class CadMotivoParada(models.Model):
    motivo                  = models.CharField(max_length=40,blank=True)

class CadFornecedor(models.Model):
    razao_social = models.CharField(max_length=50,blank=True)
    endereco     = models.CharField(max_length=50,blank=True)
    telefone     = models.CharField(max_length=20,blank=True)
    email        = models.CharField(max_length=25,blank=True)
    cnpj         = models.CharField(max_length=20,blank=True)
    estado       = models.CharField(max_length=2,blank=True)
    pais         = models.CharField(max_length=20,blank=True)
    cep          = models.CharField(max_length=15,blank=True)

class CadProduto(models.Model):
    fornecedor          = models.CharField(max_length=50,blank=True)
    comprimento_tora    = models.CharField(max_length=50,blank=True)
    largura_capa        = models.CharField(max_length=50,blank=True)
    comprimento_capa    = models.CharField(max_length=50,blank=True)
    espessura_capa      = models.CharField(max_length=50,blank=True)
    qualidade_capa      = models.CharField(max_length=50,blank=True)

        
    