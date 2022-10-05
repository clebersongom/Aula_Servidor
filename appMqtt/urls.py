from django.urls import URLPattern, path
from . import  views 

urlpatterns = [ # em minusculo

    path('mqtt', views.mqtt, name = 'mqtt'), 
    
    
]