from email.policy import default
from django.db import models
from django.utils import timezone

class DadosSecador(models.Model):
    data = models.DateTimeField(default=timezone.now)
    temperatura = models.IntegerField()
    pressao = models.IntegerField()
    umidade = models.IntegerField()
    
    

