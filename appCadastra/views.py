from ast import Not
from asyncio.windows_events import NULL
import email
from itertools import pairwise
from turtle import update
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from appCadastra.models import CadastroOp
from appCadastra.models import CadFornecedor
from appCadastra.models import CadMotivoParada
from appCadastra.models import CadProduto
from appProducao.models import ProducaoOnLine
from appProducao.models import MaquinaParada
from django.db.models import Q
from datetime import datetime 
from appCadastra.models import CadMotivoParada


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
            op = request.POST['op']
            print(op)
            
            atualiza = CadastroOp.objects.filter(numero_op = op).update(status = 'producao')
            atualiza_tab_paradas = MaquinaParada.objects.filter(op = op).update(status = 'producao')
            
            return redirect('app_home')
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
    else:
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
        

    

