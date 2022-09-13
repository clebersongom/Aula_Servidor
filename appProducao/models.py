from email.policy import default
from django.db import models
from django.utils import timezone

class ProducaoOnLine(models.Model):
    prod_online              = models.CharField(max_length=20,blank=True)# Limitendo a quantidade de caracteres
    acum_maq_parada          = models.CharField(max_length=20,blank=True)# soma do tempo de máquina parada
    
class MaquinaParada(models.Model):
    data_parada              = models.CharField(max_length=20,blank=True)# parada da máquina
    data_retorno             = models.CharField(max_length=20,blank=True)# Retorno do máquina    
    justificativa            = models.CharField(max_length=2000,blank=True)