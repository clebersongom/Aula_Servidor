from django.urls import URLPattern, path
from . import  views 

urlpatterns = [ # em minusculo

    path('', views.index, name ="app_consulta"),
    path('pesqOP', views.pesqOP, name ="pesquisaOP")
]