from dataclasses import dataclass
from itertools import count
from multiprocessing.util import is_exiting
from queue import Empty
from sqlite3 import Timestamp
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from appCadastra.models import CadastroOp
from appCadastra.models import CadTurno
from appProducao.models import MaquinaParada
from django.utils import timezone
from datetime import datetime, timedelta
from appCadastra.models import StatusOP
from appProducao.models import ProducaoOnLine
from django.db.models import Q
import time

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
                )                
                paradas.save()
                hora = time.strftime("%H:%M")                
                bc_turno  = CadTurno.objects.filter(Q(hora1__lte = hora),Q(hora12__gte = hora))#Pegar hora atual entre hora 1 e hora 12
                print('antes do if')                
                if bc_turno:  
                    print('depois do if')                  
                    data = time.strftime("%d/%m/%Y")
                    for turno in bc_turno:
                        turno.turno
                    status = StatusOP(
                        op            = abrir_op,
                        status        = 'producao', 
                        turno_ini     = turno.turno,
                        turno_fim     = '',
                        data          = data,
                        hora          = hora
                    )
                    status.save()
                op_aberta = CadastroOp.objects.filter(status = 'producao') # busca OP em produção
                opsCadastradas = CadastroOp.objects.filter(Q(hora_inicio_prod = ''), ~Q(status = 'cancelado')) 
                opsIniciadas = CadastroOp.objects.filter( Q(status = 'parado'), ~Q(hora_inicio_prod = '') )# busca se diferente de '' 
                prod_online = ProducaoOnLine.objects.filter(~Q(prod_online = 0))
                if prod_online:
                    return render(request, 'home/index.html',{'opsCadastradas': opsCadastradas,'opsIniciadas': opsIniciadas,'op_aberta':op_aberta,'prod_online':prod_online})
                else:
                    return render(request, 'home/index.html',{'opsCadastradas': opsCadastradas,'opsIniciadas': opsIniciadas,'op_aberta':op_aberta})
                                        
            else:        
                return redirect('app_home')
        return redirect('app_home')        
         
def justificaParada(request):
    pass           

