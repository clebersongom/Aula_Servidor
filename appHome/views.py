from queue import Empty
from sqlite3 import Timestamp
from django.shortcuts import render
from appCadastra.models import CadastroOp
from django.db.models import Q

def index(request):
    if request.method == 'POST':
        
        abrir_op = request.POST['abrir_op']
        atualiza =CadastroOp.objects.filter(numero_op = abrir_op).update(hora_inicio_prod = '2020')
        op_aberta = CadastroOp.objects.filter(numero_op = abrir_op)
    else:
        op_aberta = ''   

    opsCadastradas = CadastroOp.objects.filter(hora_inicio_prod = '') # busca se diferente de ''
    opsIniciadas = CadastroOp.objects.filter(~Q(hora_inicio_prod = ''))
    return render(request, 'home/index.html',{'opsCadastradas': opsCadastradas,'opsIniciadas': opsIniciadas,'op_aberta': op_aberta})
