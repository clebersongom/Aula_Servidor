from queue import Empty
from sqlite3 import Timestamp
from django.shortcuts import render,redirect
#from appCadastra.models import CadastroOp
from appProducao.models import ProducaoOnLine
from django.db.models import Q


def index(request):
    pass
    """consulta = ProducaoOnLine.objects.all()
    if not consulta:
        prod = 0
        return render(request, 'home/index.html',{'prod': prod})
    else:
        prod = consulta
        return render(request, 'home/index.html',{'prod': prod})"""
