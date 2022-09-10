

from unittest.util import _MAX_LENGTH
from django import forms



class FormCadOp(forms.Form):
    op = forms.CharField(max_length=30)
    fornecedor = forms.CharField(max_length=30)
    largura = forms.CharField(max_length=30)
    comprimento = forms.CharField(max_length=30)
    espessura = forms.CharField(max_length=30)
    producao = forms.CharField(max_length=30)
    qualidade = forms.CharField(max_length=30)  
    prioridade = forms.CharField(max_length=30)