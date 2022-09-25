from itertools import count
from multiprocessing.util import is_exiting
from queue import Empty
from sqlite3 import Timestamp
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from appCadastra.models import CadastroOp
from appProducao.models import MaquinaParada
from django.utils import timezone
from datetime import datetime, timedelta

#from appProducao.models import ProducaoOnLine
from django.db.models import Q

def index(request):    
    op_aberta = CadastroOp.objects.filter(status = 'producao') # busca OP em produção
    opsCadastradas = CadastroOp.objects.filter(Q(hora_inicio_prod = ''), ~Q(status = 'cancelado')) 
    opsIniciadas = CadastroOp.objects.filter( Q(status = 'parado'), ~Q(hora_inicio_prod = '') )# busca se diferente de '' 
       
    return render(request, 'home/index.html',{'opsCadastradas': opsCadastradas,'opsIniciadas': opsIniciadas,'op_aberta':op_aberta})

def inserirOP(request):
    if request.method == 'POST':
        if request.POST['abrir_op'] != 'Sem Ops':
            consulta = CadastroOp.objects.filter(status = 'producao')
             
            if not consulta:
                abrir_op = request.POST['abrir_op']
                atualiza =CadastroOp.objects.filter(numero_op = abrir_op).update(hora_inicio_prod = '2020' ,status ='producao')                
                paradas = MaquinaParada(
                    op            = abrir_op,
                    status        = 'producao',
                    #data_parada   = datetime.now(),
                )
                paradas.save()
                return redirect('app_home')
            else:        
                return redirect('app_home')
        return redirect('app_home')        
         
def justificaParada(request):
    pass           