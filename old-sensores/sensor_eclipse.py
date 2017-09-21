# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import random
import Adafruit_DHT
from datetime import datetime

#Servidor Local
#MQTT_ADDRESS = '192.168.50.106'
#MQTT_PORT = 8883
# descomente esta linha para usar o servidor da Fundação Eclipse.
MQTT_ADDRESS = 'iot.eclipse.org'
MQTT_PORT = 1883
MQTT_TIMEOUT = 60
UNIDADE = 'MG'
SETOR = 'TI'
SENSOR = 'RP01'


def send_message():
    client = mqtt.Client()
    # descomente esta linha caso seu servidor possua autenticação.
    #client.username_pw_set('ticimed', 'cimed@2017')
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)

    #faz a leitura do sensor
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
    time = str( datetime.now() )
    send_msg = {
        'datahora': time,
	'temperatura': temperature,
	'umidade': humidity
    }

    canal = UNIDADE+'/'+SETOR+'/'+SENSOR
    result, mid = client.publish(canal, payload=json.dumps(send_msg), qos=1)
    print('Mensagem enviada ao canal: %d' % mid)

if __name__ == '__main__':
    send_message()
