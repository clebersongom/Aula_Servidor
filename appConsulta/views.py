from django.shortcuts import render
from appCadastra.models import CadastroOp

def index(request):
    return render(request, 'consulta/index.html')



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
           

    
  
