from datetime import datetime
from email.policy import default
from django.db import models
from django.utils import timezone

class ProducaoOnLine(models.Model):
    prod_online              = models.CharField(max_length=20,blank=True)# Limitendo a quantidade de caracteres
    acum_maq_parada          = models.CharField(max_length=20,blank=True)# soma do tempo de máquina parada
    
class MaquinaParada(models.Model):
    op                       = models.CharField(max_length=5000,blank=True)
    data_parada              = models.DateTimeField(default='1000-01-01 00:00:00.000000')# parada da máquina
    data_retorno             = models.DateTimeField(default='1000-01-01 00:00:00.000000')# Retorno do máquina    
    justificativa            = models.CharField(max_length=5000,blank=True)
    observacao               = models.CharField(max_length=1000,blank=True)
    status                   = models.CharField(max_length=5000)