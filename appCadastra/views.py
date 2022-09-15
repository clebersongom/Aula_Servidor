from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from appCadastra.models import CadastroOp


def index(request):
    # recebendo via POST os dados do formulário
    if request.method == 'POST':  # verificando se há um POST
        op          = request.POST['cad_op']
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
        opsCadastradas = CadastroOp.objects.all()
        return render(request, 'cadastro/index.html',{'opsCadastradas': opsCadastradas})

    #consultando OPs cadastradas no banco e enviando para o template      
    opsCadastradas = CadastroOp.objects.all()

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
        op = request.POST['op']
        atualiza = CadastroOp.objects.filter(numero_op = op).update(status = 'producao')
        return redirect('app_home')