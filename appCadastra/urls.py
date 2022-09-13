from django.urls import URLPattern, path
from . import  views 


urlpatterns = [ # em minusculo

    path('', views.index, name ="app_cadastro"),
    path('paraOP/', views.para_op, name ="para_op"),
    path('finalizaOP/', views.finaliza_op, name ="finaliza_op")
]