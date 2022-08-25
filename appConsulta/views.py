from django.shortcuts import render
from appConsulta.models import DadosSecador

def index(request):
    dadosSecador = DadosSecador.objects.all() 
    teste = [50,25]
    
    
    return render(request, 'consulta/index.html', {'dadosSecador' : dadosSecador, 'teste': teste})
  
