from asyncio.windows_events import NULL
from contextlib import nullcontext
from pyexpat import model
from django.shortcuts import render
from appCadastra.models import CadastroOp

from .forms import FormCadOp



def index(request):
    
    
    if request.method == 'POST':  
        op          = request.POST['cad_op']
        fornecedor  = request.POST['cad_fornecedor']
        largura     = request.POST['cad_Largura']
        comprimento = request.POST['cad_comprimento']
        espessura   = request.POST['cad_espessura']
        producao    = request.POST['cad_producao']
        qualidade   = request.POST['cad_qualidade']
        prioridade  = request.POST['cad_prioridade']
        #hora_ini    = request.POST['hora_ini']
        #hora_final  = request.POST['hora_fim']

        cadastrar = CadastroOp(
            numero_op           = op,
            fornecedor          = fornecedor,
            largura_capa        = largura,
            comprimento_capa    = comprimento,
            expessura_capa      = espessura,
            qualidade_capa      = qualidade,
            quantidade_producao = producao,
            prioridade          = prioridade, 
           # hora_inicio_prod    = hora_ini,
           # hora_fim_prod       = hora_final
            )
        cadastrar.save()
        return render(request, 'cadastro/index.html')
        
    return render(request, 'cadastro/index.html')

        #form = FormCadOp(request.POST)        
        #if form.is_valid():
            #form.save() 
            #return render(request, 'cadastro/index.html')
        
       # return render(request, 'cadastro/index.html',{'form': form})
       
        
    #return render(request, 'cadastro/index.html',{'form': form})    

        
        
        
    
    
   

    
