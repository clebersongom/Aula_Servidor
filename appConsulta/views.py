from django.shortcuts import render
from appConsulta.models import DadosSecador

def index(request):
    dadosSecador = DadosSecador.objects.all()   
    return render(request, 'consulta/index.html', {'dadosSecador' : dadosSecador})
  
