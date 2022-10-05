from django.shortcuts import render
from appProducao.models import ProducaoOnLine
import paho.mqtt.client as mqtt
import json
import MySQLdb
from datetime import datetime
import sys

# Abrir conexión con bases de datos
try:
    db = MySQLdb.connect("127.0.0.1","root","root","db_secador")
except:
    print("No se pudo conectar con la base de datos")
    print("Cerrando...")
    sys.exit()

# Preparando cursor
cursor = db.cursor()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Conectado - Codigo de resultado: "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("data/sec1/tempos1/5111848698113559551")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #  print(msg.topic+" "+str(msg.payload))
    #  lista = str(msg.payload).split("b")
    msgjson = json.loads(msg.payload)

    # Extrair os valores json que chegam no tópico MQTT
    #  tmpEvento = datetime.strptime(msgjson['_terminalTime'], '%Y-%m-%d %H:%M:%S.%f')
    tmpEvento = msgjson['_terminalTime']
    maq = msgjson['_groupName']
    hora = msgjson['Hora']
    minuto = msgjson['Minute']
    seg = msgjson['Second']
    
    #  sql = """INSERT INTO db_secador.teste1 (id, maquina, hora, minuto, segundo, time stamp) VALUES (NULL, '""" + maq + """', '""" + hora + """', '""" + minuto + """', '""" + seg + """', '""" + tmpEvento + """');"""
    
    
    
    try:
        # Ejecutar un comando SQL
        #  cursor.execute(sql)
        #  db.commit()
        #  print("Guardando en base de datos...OK")

        dadosProd = ProducaoOnLine(
            prod_online = seg,
            acum_maq_parada = minuto
        )
        dadosProd.save()

    except:
        db.rollback()
        print("Guardando en base de datos...Falló")
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("127.0.0.1", 1883, 60)
except:
    print("No se pudo conectar con el MQTT Broker...")
    print("Cerrando...")
    db.close()
    sys.exit()   
    
#  client.username_pw_set("lqeamtbn", "vh0cU_Vcszxp")

try:
    client.loop_forever()
except KeyboardInterrupt:  #precionar Crtl + C para salir
    print("Cerrando...")
    db.close()


    