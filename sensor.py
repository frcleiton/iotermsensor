# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import random
import ConfigParser
from datetime import datetime

#Servidor Local
MQTT_ADDRESS = '192.168.50.106'
MQTT_PORT = 8883
MQTT_TIMEOUT = 60
SENSOR_ID = 'RP01'
DEBUG = True

config = ConfigParser.ConfigParser()
config.read('sensor.cfg')
nome_disp = config.get('config','dispositivo')
plataforma = config.get('config','plataforma')
if (nome_disp):
	SENSOR_ID = nome_disp
if (plataforma):
	MQTT_ADDRESS = plataforma

client = mqtt.Client()

def publish_value(_temperature, _humidity):

	client.username_pw_set('ticleiton', 'ti@cleiton')
	client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)

	str_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	temp_topic = SENSOR_ID+'/temperature'
	humi_topic = SENSOR_ID+'/humidity'

	if _temperature is not None:
		send_msg = {'t': str_time,
					'mu': 'C',
					'value': _temperature}
		result, mid = client.publish(temp_topic, payload=json.dumps(send_msg), qos=1, retain=True )
		print "%s - %s" % (temp_topic, send_msg)

	if _humidity is not None:
		send_msg = {'t': str_time,
					'mu': 'RH',
					'value': _humidity}
		result, mid = client.publish(humi_topic, payload=json.dumps(send_msg), qos=1, retain=True )
		print "%s - %s" % (humi_topic, send_msg)


def read_sensor():

	#faz a leitura do sensor
    if not DEBUG:
        import Adafruit_DHT
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
    else:
        temperature = round(random.randint(0, 40)+random.random(),2)
        humidity = round(random.randint(0, 100)+random.random(),2)

	publish_value(round(temperature,2), round(humidity,0))

if __name__ == '__main__':
	read_sensor()
