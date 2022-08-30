from django.shortcuts import render

def index(request):

    # aqui código para salvar no banco de dados 


    return render(request, 'cadastro/index.html')
