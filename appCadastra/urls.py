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
    path('editaJustificativa/',views.editaJustificativa, name='editaJustificativa')
    
]