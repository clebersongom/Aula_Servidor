from django.urls import URLPattern, path
from . import  views 


urlpatterns = [ # em minusculo

    path('', views.index, name ="app_cadastro")
]