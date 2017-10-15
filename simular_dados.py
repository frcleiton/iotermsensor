# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import random
import ConfigParser
from datetime import date, datetime, timedelta

config = ConfigParser.ConfigParser()
config.read('sensor.cfg')

#Servidor Local
MQTT_ADDRESS    = config.get('config','plataforma')
MQTT_PORT       = config.get('config','porta')
MQTT_TIMEOUT    = 60
SENSOR_ID       = config.get('config','dispositivo')
DEBUG           = config.get('config','mododebug')

client = mqtt.Client()
client.username_pw_set('ticleiton', 'ti@cleiton')
client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)

def publish_value(_temperature, _humidity, _str_time):

	temp_topic = SENSOR_ID+'/temperature'
	humi_topic = SENSOR_ID+'/humidity'

	if _temperature is not None:
		send_msg = {'t': _str_time,
					'mu': 'C',
					'value': _temperature}
		result, mid = client.publish(temp_topic, payload=json.dumps(send_msg), qos=0, retain=True )
		print "%s - %s" % (temp_topic, send_msg)

	if _humidity is not None:
		send_msg = {'t': _str_time,
					'mu': 'RH',
					'value': _humidity}
		result, mid = client.publish(humi_topic, payload=json.dumps(send_msg), qos=0, retain=True )
		print "%s - %s" % (humi_topic, send_msg)


def read_sensor():

	data_hora_gerada = datetime.now() - timedelta(days=1)
	agora = datetime.now()
		
	for i in range(50000):
		str_time = data_hora_gerada.strftime("%d-%m-%Y %H:%M:%S")
		temperature = round(random.randint(20, 25)+random.random(),2)
		humidity = round(random.randint(40, 60)+random.random(),2)
		publish_value(round(temperature,2), round(humidity,0), str_time)
		print i
		data_hora_gerada = data_hora_gerada + timedelta(minutes=1)
		if data_hora_gerada >= agora:
			break
		

if __name__ == '__main__':
	read_sensor()
