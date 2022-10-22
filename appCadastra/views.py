from ast import Not
from asyncio.windows_events import NULL
import email
from itertools import pairwise
from os import times
from sqlite3 import Time, Timestamp
from time import time
from turtle import update
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from appCadastra.models import CadastroOp
from appCadastra.models import CadFornecedor
from appCadastra.models import CadMotivoParada
from appCadastra.models import CadTurno
from appCadastra.models import StatusOP
from appCadastra.models import HoraHora
from appCadastra.models import CadProduto
from appProducao.models import ProducaoOnLine
from appProducao.models import MaquinaParada
from django.db.models import Q
from datetime import datetime 
from appCadastra.models import CadMotivoParada
import time
from appCadastra.models import HoraTabela


def index(request):
    # recebendo via POST os dados do formulário
    if request.method == 'POST':  # verificando se há um POST
        op          = request.POST['cad_op']
        consulta = CadastroOp.objects.filter(numero_op = op)
        if not consulta and op != '':
            fornecedor  = request.POST['cad_fornecedor']
            largura     = request.POST['cad_Largura']
            comprimento = request.POST['cad_comprimento']
            espessura   = request.POST['cad_espessura']
            producao    = request.POST['cad_producao']
            qualidade   = request.POST['cad_qualidade']  
                       
            # Enviando os valores do formulario para classe MODEL
            cadastrar = CadastroOp(
                numero_op           = op,
                fornecedor          = fornecedor,
                largura_capa        = largura,
                comprimento_capa    = comprimento,
                expessura_capa      = espessura,
                qualidade_capa      = qualidade,
                quantidade_producao = producao, 
                )
            #salvando os valores no banco 
            cadastrar.save()
            cadastra_sucess = True
            opsCadastradas = CadastroOp.objects.filter(~Q(status = 'cancelado'))
            fornecedor = CadFornecedor.objects.all()  
            produto    = CadProduto.objects.all() 
            return render(request, 'cadastro/index.html',{'opsCadastradas': opsCadastradas, 'cadastra_sucess' : cadastra_sucess,'fornecedor': fornecedor,'produto':produto})
        else:
            mensagem = True # gera a mensagem de erro quando OP já está cadastrada no sistema
            opsCadastradas = CadastroOp.objects.filter(~Q(status = 'cancelado'))
            return render(request, 'cadastro/index.html',{'opsCadastradas': opsCadastradas,'mensagem':mensagem})
    else:  
        fornecedor = CadFornecedor.objects.all()  
        produto    = CadProduto.objects.all() 
        opsCadastradas = CadastroOp.objects.filter(~Q(status = 'cancelado'))#consultando OPs cadastradas no banco e enviando para o template
        return render(request, 'cadastro/index.html',{'opsCadastradas': opsCadastradas, 'fornecedor': fornecedor,'produto':produto})

def para_op(request):
    if request.method == 'POST':        
        op = request.POST['op'] 
        atualiza = CadastroOp.objects.filter(numero_op = op).update(status = 'parado')
        atualiza_tab_paradas = MaquinaParada.objects.filter(op = op).update(status = 'parado')
        return redirect('app_home')
        
def finaliza_op(request):
    if request.method == 'POST':        
        op = request.POST['op']  
        atualiza = CadastroOp.objects.filter(numero_op = op).update( hora_fim_prod = '2022', status = 'finalizado')
        atualiza_tab_paradas = MaquinaParada.objects.filter(op = op).update(status = 'finalizado')
        return redirect('app_home')
        
        
def abre_Op_parada(request):
    if request.method == 'POST':
        consulta = CadastroOp.objects.filter(status = 'producao')
        
        if not consulta:   
            prod_online = ProducaoOnLine.objects.filter(~Q(prod_online = 0)) 
            if not prod_online: 
                op = request.POST['op']
                atualiza = CadastroOp.objects.filter(numero_op = op).update(status = 'producao')
                atualiza_tab_paradas = MaquinaParada.objects.filter(op = op).update(status = 'producao')
                op_aberta = CadastroOp.objects.filter(status = 'producao') # busca OP em produção
                opsCadastradas = CadastroOp.objects.filter(Q(hora_inicio_prod = ''), ~Q(status = 'cancelado')) 
                opsIniciadas = CadastroOp.objects.filter( Q(status = 'parado'), ~Q(hora_inicio_prod = '') )
                return redirect('app_home')
            else:    
                op = request.POST['op']
                atualiza = CadastroOp.objects.filter(numero_op = op).update(status = 'producao')
                atualiza_tab_paradas = MaquinaParada.objects.filter(op = op).update(status = 'producao')
                op_aberta = CadastroOp.objects.filter(status = 'producao') # busca OP em produção
                opsCadastradas = CadastroOp.objects.filter(Q(hora_inicio_prod = ''), ~Q(status = 'cancelado')) 
                opsIniciadas = CadastroOp.objects.filter( Q(status = 'parado'), ~Q(hora_inicio_prod = '') )# busca se diferente de '' 
                prod_online = ProducaoOnLine.objects.filter(~Q(prod_online = 0))
                return render(request, 'home/index.html',{'opsCadastradas': opsCadastradas,'opsIniciadas': opsIniciadas,'op_aberta':op_aberta,'prod_online':prod_online})
                
            
        else:            
            return redirect('app_home')   

def editarOP(request):
    if request.method == 'POST':
        op = request.POST['editar']
        consulta = CadastroOp.objects.filter(numero_op = op)
        #return redirect('app_cadastro')
        return render(request, 'cadastro/consulta.html',{'consulta': consulta})
def atualizarOP(request):   
    if request.method == 'POST':
        op          = request.POST['edit_op']
        consulta = CadastroOp.objects.filter(numero_op = op)
        if consulta:
            fornecedor  = request.POST['edit_fornecedor']
            largura     = request.POST['edit_largura']
            comprimento = request.POST['edit_comprimento']
            espessura   = request.POST['edit_espessura']
            producao    = request.POST['edit_producao']
            qualidade   = request.POST['edit_qualidade']
            status      = request.POST['edit_status']  
            consulta.update(
                numero_op           = op,
                fornecedor          = fornecedor,
                largura_capa        = largura,
                comprimento_capa    = comprimento,
                expessura_capa      = espessura,
                qualidade_capa      = qualidade,
                quantidade_producao = producao, 
                status              = status,
                )
            atualiza_sucess = True
            return render(request, 'cadastro/consulta.html',{'consulta': consulta, 'atualiza_sucess' : atualiza_sucess})
    return redirect('app_cadastro')  

def cancelarOP(request):     
    if request.method == 'POST':
        op = request.POST['cancelarOP']
        consulta = CadastroOp.objects.filter(numero_op = op)
        if consulta:
            #consulta.delete()
            consulta.update(status = 'cancelado')
            cancelado_sucess = True
            opsCadastradas = CadastroOp.objects.filter(~Q(status = 'cancelado'))
            return render(request, 'cadastro/consulta.html',{'opsCadastradas': opsCadastradas,'cancelado_sucess':cancelado_sucess})
        else:
            return redirect('consultaOP') 
    
    return redirect('consultaOP')
        
def producaoOP(request):
    if request.method == "POST":
        zerar = request.POST['zerar']
        producao = ProducaoOnLine.objects.all().update(prod_online = zerar)
        return redirect('app_home')
    else: # entra no laço a cada 3 segundos javaScript
        consulta_prod = ProducaoOnLine.objects.all()
        return render(request,'cadastro/producao.html',{'consulta_prod':consulta_prod})

def paradasOP(request):
    op_producao = CadastroOp.objects.filter(Q(status = 'producao'))
    if op_producao:        
        for op in op_producao:
            if op.numero_op:                
                consul_parada = MaquinaParada.objects.filter(Q(status = 'producao'),~Q(data_parada = '1000-01-01 00:00:00.000000'),~Q(data_retorno = '1000-01-01 00:00:00.000000'),Q(justificativa = ''), Q(op = op.numero_op))# condicional da OP igual da produção
                
                if consul_parada:                                       
                    return render(request,'cadastro/paradas.html',{'consul_parada': consul_parada})        
                else:                    
                    return render(request,'cadastro/paradas.html')
            else:
                return render(request,'cadastro/paradas.html')        
    else:
        return render(request,'cadastro/paradas.html')

def justificaParada(request):  
    op_producao = CadastroOp.objects.filter(Q(status = 'producao'))
    if op_producao:
        for op in op_producao:
            if op.numero_op:
                cons_justifica = MaquinaParada.objects.filter(Q(status = 'producao'),~Q(data_parada = '1000-01-01 00:00:00.000000'),~Q(data_retorno = '1000-01-01 00:00:00.000000'),Q(justificativa = ''), Q(op = op.numero_op))# condicional da OP igual da produção
                motivos        = CadMotivoParada.objects.all()
                
                return render(request,'cadastro/justifica.html',{'cons_justifica': cons_justifica,'motivos': motivos})
            else:
                return render(request,'cadastro/justifica.html')  
        else:
             return render(request,'cadastro/justifica.html')   
    else:
         return render(request,'cadastro/justifica.html')    

def editaJustificativa(request):
    if request.method == 'POST':       
        id            = request.POST['id'] 
        just          = request.POST['edit_just'] # criar mais um campo que aceite null na tabela para just (outros)
        motivo        = request.POST['motivo'] 
        consjustifica = MaquinaParada.objects.filter(Q(id = id)).update(justificativa = motivo,observacao  = just)# condicional da OP igual da produção
        
        cons_justifica = MaquinaParada.objects.filter(Q(status = 'producao'),~Q(data_parada = '1000-01-01 00:00:00.000000'),~Q(data_retorno = '1000-01-01 00:00:00.000000'),Q(justificativa = ''))# condicional da OP igual da produção
        
        motivos        = CadMotivoParada.objects.all()
        return render(request,'cadastro/justifica.html',{'cons_justifica': cons_justifica,'motivos': motivos })

#def cad_produto(request):    
    #return render(request, 'cadastro/produto.html')

def consultaOP(request):
    if request.method == 'POST':
        op          = request.POST['pesqOP']
        consultaOP = CadastroOp.objects.filter(numero_op = op)
        if consultaOP and consultaOP!='':
            print('entrou')
            return render(request, 'cadastro/consulta.html', {'consultaOP' : consultaOP })
        else:
            semOP = True
            return render(request, 'cadastro/consulta.html',{'semOP' : semOP})   
    opsCadastradas = CadastroOp.objects.filter(~Q(status = 'cancelado'))#consultando OPs cadastradas no banco e enviando para o template
    
    return render(request, 'cadastro/consulta.html',{'opsCadastradas': opsCadastradas})

def pesqOP(request):
    if request.method == 'POST':
        op          = request.POST['pesqOP']
        consultaOP = CadastroOp.objects.filter(numero_op = op)
        if consultaOP and consultaOP!='':
            print('entrou')
            return render(request, 'cadastro/index.html', {'consultaOP' : consultaOP })
        else:
            semOP = True
            return render(request, 'cadastro/index.html',{'semOP' : semOP}) 
def pag_parada(request):
    return render(request, 'cadastro/cad_paradas.html')
      
def cadastro_paradas(request):
    if request.method =='POST':
        cad = request.POST['cad_parada']
        motivo_parada = CadMotivoParada(
            motivo      = cad            
        )

        motivo_parada.save()
        mens = True
        return render(request, 'cadastro/cad_paradas.html', {'mens' : mens})
        
    return render(request, 'cadastro/cad_paradas.html')
    
def cad_fornecedor(request):
    if not request.method == 'POST':
        return render(request,'cadastro/fornecedor.html')
    else:
        cad_razao_social = request.POST['cad_razao_social']
        cad_endereco     = request.POST['cad_endereco']
        cad_telefone     = request.POST['cad_telefone']
        cad_email        = request.POST['cad_email']
        cad_cnpj         = request.POST['cad_cnpj']
        cad_estado       = request.POST['cad_estado']
        cad_pais         = request.POST['cad_pais']
        cad_cep          = request.POST['cad_cep']
        
        cadastro = CadFornecedor(
            razao_social = cad_razao_social,
            endereco     = cad_endereco,
            telefone     = cad_telefone,
            email        = cad_email,
            cnpj         = cad_cnpj,
            estado       = cad_estado,
            pais         = cad_pais,
            cep          = cad_cep
        )
        cadastro.save()
        mens = True
        return render(request,'cadastro/fornecedor.html',{'mens':mens})

def cad_produto(request):
    if not request.method == 'POST':  
        fornecedor = CadFornecedor.objects.all() 
        return render(request,'cadastro/cad_produto.html',{'fornecedor':fornecedor})        
    else:
        fornecedor          = request.POST['fornecedor']
        cad_comp_tora       = request.POST['cad_comp_tora']
        cad_larg_capa       = request.POST['cad_larg_capa']
        cad_comp_capa       = request.POST['cad_comp_capa']
        cad_espess_capa     = request.POST['cad_espess_capa']
        cad_qualidade_capa  = request.POST['cad_qualidade_capa']
        cadastrar_prod = CadProduto(
            fornecedor              = fornecedor,   
            comprimento_tora        = cad_larg_capa,
            largura_capa            = cad_comp_tora,
            comprimento_capa        = cad_comp_capa,
            espessura_capa          = cad_espess_capa,
            qualidade_capa          = cad_qualidade_capa
        ) 
        cadastrar_prod.save()
        mens = True
        fornecedor = CadFornecedor.objects.all() 
        return render(request,'cadastro/cad_produto.html',{'mens':mens,'fornecedor':fornecedor})
# Cadastro de hora inicial e final na tabela do banco de dados       
def cad_horas_trab(request):
    if not request.method == 'POST': 
        return render(request,'cadastro/horas_trabalho.html')
    else:
        turno       = request.POST['turno']
        hora1    = request.POST['hora1']
        hora2    = request.POST['hora2']
        hora3    = request.POST['hora3']
        hora4    = request.POST['hora4']
        hora5    = request.POST['hora5']
        hora6    = request.POST['hora6']
        hora7    = request.POST['hora7']
        hora8    = request.POST['hora8']
        hora9    = request.POST['hora9']
        hora10   = request.POST['hora10']
        hora11   = request.POST['hora11']
        hora12   = request.POST['hora12']
       
        cad_turno = CadTurno(
            turno           = turno,
            hora1           = hora1,
            hora2           = hora2,
            hora3           = hora3,
            hora4           = hora4,
            hora5           = hora5,
            hora6           = hora6,
            hora7           = hora7,
            hora8           = hora8,
            hora9           = hora9,
            hora10          = hora10,
            hora11          = hora11,
            hora12          = hora12
        )
        cad_turno.save()
        mens = True
        return render(request,'cadastro/horas_trabalho.html',{'mens' : mens})
def hora_hora(request): 
    hora = time.strftime("%H:%M")# pego hora e minuto 
    data = time.strftime("%d/%m/%Y")
    bc_hr  = CadTurno.objects.filter(
    Q(hora1 = hora)|
    Q(hora2 = hora)|
    Q(hora3 = hora)|
    Q(hora4 = hora)|
    Q(hora5 = hora)|
    Q(hora6 = hora)|
    Q(hora7 = hora)|
    Q(hora8 = hora)|
    Q(hora9 = hora)|
    Q(hora10 = hora)|
    Q(hora11 = hora)|
    Q(hora12 = hora)
    )  
    if not bc_hr: # se busca hora não obter resultado    
        bc_turno = StatusOP.objects.filter(status = 'producao')   
        for bc_t in bc_turno:
            bc_t.turno_ini
        busca_data  = HoraHora.objects.filter(Q(data = data),Q(turno = bc_t.turno_ini))# ***Criar uma tabela de status onde requer turno para inserir nessa consulta
        if not busca_data: # se bausca data não encontrar data atual retorna página sem variável 
            return render(request,'cadastro/hora_hora.html')
        else:# se busca data existe retorna página váriavel com data atual           
            return render(request,'cadastro/hora_hora.html',{'busca_data':busca_data})
    else:                      
        prod_online = ProducaoOnLine.objects.all()
        for po in prod_online:
            po.prod_online           
        op_producao = CadastroOp.objects.filter(Q(status = 'producao'))
        for op in op_producao:
            op.numero_op
        for valor in bc_hr:            
            valor.turno           
        HoraXHora = HoraHora( # salvar no HoraHora com turno, hora, produção e OP,HoraHora
        op               = op.numero_op,
        prod_online      = po.prod_online,     
        data             = data,
        hora             = hora,
        turno            = valor.turno
        )              
        HoraXHora.save()   
        busca_data  = HoraHora.objects.filter(Q(data = data),Q(turno = valor.turno))   
        return render(request,'cadastro/hora_hora.html',{'busca_data':busca_data})  
        

    #return render(request,'cadastro/hora_hora.html')
    """"
    status = CadastroOp.objects.filter(Q(status = 'producao')) # consulta se tem OP em produção
    if not status:        
        return render(request,'cadastro/hora_hora.html')
    else:  
        data = time.strftime("%d/%m/%Y")
        busca_data  = HoraHora.objects.filter(data = data) 
        if not busca_data:           
            return render(request,'cadastro/hora_hora.html')
        else:
            hora = time.strftime("%H:%M")# pego hora, minuto e segundo atuais
            #busca_hora  = CadTurno.objects.all()     
            for d in busca_data:
                if  d.hora == hora:
                    return render(request,'cadastro/hora_hora.html',{'busca_horahora':busca_data})
                else:
                    return render(request,'cadastro/hora_hora.html')"""

    """else:
        data = time.strftime("%d/%m/%Y") 
        hora = time.strftime("%H:%M")# pego hora, minuto e segundo atuais
        busca_hora  = CadTurno.objects.filter(hora1 = hora)       
        prod_online = ProducaoOnLine.objects.all()
        for po in prod_online:
            po.prod_online           
        op_producao = CadastroOp.objects.filter(Q(status = 'producao'))
        for op in op_producao:
            op.numero_op
        for valor in busca_hora:            
            valor.turno
        #hora_anterior = HoraHora.objects.filter(turno = valor.turno).order_by('id').latest('id')
        #obj = Model.objects.filter(testfield=12).order_by('id').latest('id')    
        HoraXHora = HoraHora( # salvar no HoraHora com turno, hora, produção e OP,HoraHora
            op               = op.numero_op,
            prod_online      = po.prod_online,     
            data             = data,
            hora             = hora,
            turno            = valor.turno
            )              
        HoraXHora.save()        
        return render(request,'cadastro/hora_hora.html')"""
        

