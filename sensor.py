# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import random
import ConfigParser
from datetime import datetime

config = ConfigParser.ConfigParser()
config.read('sensor.cfg')

#Servidor Local
MQTT_ADDRESS    = config.get('config','plataforma')
MQTT_PORT       = config.get('config','porta')
MQTT_TIMEOUT    = 30
SENSOR_ID       = config.get('config','dispositivo')
DEBUG           = config.get('config','mododebug')

#client = mqtt.Client(SENSOR_ID,False)
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
		result, mid = client.publish(temp_topic, payload=json.dumps(send_msg), qos=1 )
		print "%s - %s" % (temp_topic, send_msg)

	if _humidity is not None:
		send_msg = {'t': str_time,
					'mu': 'RH',
					'value': _humidity}
		result, mid = client.publish(humi_topic, payload=json.dumps(send_msg), qos=1 )
		print "%s - %s" % (humi_topic, send_msg)


def read_sensor():

	#faz a leitura do sensor
	if DEBUG <> '1':
		import Adafruit_DHT
		humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
	else:
		temperature = round(random.randint(20, 30)+random.random(),2)
		humidity = round(random.randint(10, 60)+random.random(),2)
	#print 'publish'
	publish_value(round(temperature,2), round(humidity,0))

if __name__ == '__main__':
	read_sensor()
