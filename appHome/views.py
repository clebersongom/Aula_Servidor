from queue import Empty
from django.shortcuts import render
from appCadastra.models import CadastroOp
from django.db.models import Q

def index(request):

    opsCadastradas = CadastroOp.objects.filter(hora_inicio_prod = '') # busca se diferente de ''
    opsIniciadas = CadastroOp.objects.filter(~Q(hora_inicio_prod = ''))
    return render(request, 'home/index.html',{'opsCadastradas': opsCadastradas,'opsIniciadas': opsIniciadas})
