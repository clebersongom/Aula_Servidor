from django.shortcuts import render
from appConsulta.models import DadosSecador
import json

temp = []
pressao = []
umidade = []
dia = []


def index(request):
    dia = [730,830, 930, 1030,1130,1230,1330,1430,1530,1630,1730,1830,1930,2030,2130,2230,2330] 
    dadosSecador = DadosSecador.objects.all()  
    pressao.clear() # limpa a lista para não ir acrescentando
    temp.clear()
    umidade.clear()

    for dados in dadosSecador:
        temp.append(dados.temperatura)
        pressao.append(dados.pressao)
        umidade.append(dados.umidade)
       
    
    return render(request, 'consulta/index.html', {'pressao_Secador' : pressao, 'temperatura_secador' : temp, 'dados_banco' : dadosSecador,'umidade_secador':umidade, 'dia':dia})
    
  
