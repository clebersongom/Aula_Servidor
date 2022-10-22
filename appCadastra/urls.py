from django.urls import URLPattern, path
from . import  views 


urlpatterns = [ # em minusculo

    path('', views.index, name ="app_cadastro"),
    path('paraOP/', views.para_op, name ="para_op"),
    path('finalizaOP/', views.finaliza_op, name ="finaliza_op"),
    path('abreOpParada/', views.abre_Op_parada, name ="abreOp_Parada"),
    path('editarOP/', views.editarOP, name = "editarOP"),
    path('atualizar/', views.atualizarOP, name ="atualizarOP"),
    path('cancelarOP/', views.cancelarOP, name="cancelarOP"),
    path('producaoOP/', views.producaoOP, name="producaoOP"),
    path('paradasOP/', views.paradasOP, name="paradasOP"),
    path('justificaParada/',views.justificaParada, name='justificaParada'),
    path('editaJustificativa/',views.editaJustificativa, name='editaJustificativa'),
    path('cad_produto/',views.cad_produto, name='cad_produto'),
    path('consultaOP/', views.consultaOP, name ='consultaOP'),
    path('pesqOP/', views.pesqOP, name ="pesquisaOP"),
    path('pag_parada/', views.pag_parada, name ="pag_parada"),
    path('cadastro_paradas/', views.cadastro_paradas, name ="cadastro_paradas"),
    path('cad_fornecedor/', views.cad_fornecedor, name ="cad_fornecedor"),
    path('cad_horas_trab/', views.cad_horas_trab, name ="cad_horas_trab"),
    path('hora_hora/', views.hora_hora, name ="hora_hora")
    
]