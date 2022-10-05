from django.urls import URLPattern, path
from . import  views 

urlpatterns = [ # em minusculo

    path('', views.index, name = 'app_home'), 
    path('inserirOP', views.inserirOP, name = 'inserirOP'),
    path('justificaParada', views.justificaParada, name = 'justificaParada'),
   
]