from queue import Empty
from sqlite3 import Timestamp
from django.shortcuts import render,redirect
from appCadastra.models import CadastroOp
from django.db.models import Q


def index(request):
    pass