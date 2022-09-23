from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from appCadastra.models import CadastroOp
from appProducao.models import ProducaoOnLine
from django.db.models import Q


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
            return render(request, 'cadastro/index.html',{'opsCadastradas': opsCadastradas, 'cadastra_sucess' : cadastra_sucess})
        else:
            mensagem = True # gera a mensagem de erro quando OP já está cadastrada no sistema
            opsCadastradas = CadastroOp.objects.filter(~Q(status = 'cancelado'))
            return render(request, 'cadastro/index.html',{'opsCadastradas': opsCadastradas,'mensagem':mensagem})
          
    opsCadastradas = CadastroOp.objects.filter(~Q(status = 'cancelado'))#consultando OPs cadastradas no banco e enviando para o template
    return render(request, 'cadastro/index.html',{'opsCadastradas': opsCadastradas})

def para_op(request):
    if request.method == 'POST':        
        op = request.POST['op'] 
        atualiza = CadastroOp.objects.filter(numero_op = op).update( status = 'parado')
        return redirect('app_home')
        
def finaliza_op(request):
    if request.method == 'POST':        
        op = request.POST['op']  
        atualiza = CadastroOp.objects.filter(numero_op = op).update( hora_fim_prod = '2022', status = 'finalizado')
        return redirect('app_home')
        
        
def abre_Op_parada(request):
    if request.method == 'POST':
        consulta = CadastroOp.objects.filter(status = 'producao')
        if not consulta:
            op = request.POST['op']
            atualiza = CadastroOp.objects.filter(numero_op = op).update(status = 'producao')
            return redirect('app_home')
        else:            
            return redirect('app_home')   

def editarOP(request):
    if request.method == 'POST':
        op = request.POST['editar']
        consulta = CadastroOp.objects.filter(numero_op = op)
        #return redirect('app_cadastro')
        return render(request, 'cadastro/index.html',{'consulta': consulta})
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
            return render(request, 'cadastro/index.html',{'consulta': consulta, 'atualiza_sucess' : atualiza_sucess})
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
            return render(request, 'cadastro/index.html',{'opsCadastradas': opsCadastradas,'cancelado_sucess':cancelado_sucess})
        else:
            return redirect('app_cadastro') 
    
    return redirect('app_cadastro')
        
def producaoOP(request):
    consulta_prod = ProducaoOnLine.objects.all()
    return render(request,'cadastro/producao.html',{'consulta_prod':consulta_prod})