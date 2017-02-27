#Raspberry Pi Plant Monitor (via Arduino and PSoC Analog Coprocessor Pioneer Kit)
#Author: Austin Wilson

#Import packages from PubHub
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory

#Setup Serial communication between Arduino and Rspberry Pi
import serial
import json
import subprocess
import os
import threading
import time
import sys

subprocess.Popen(["nohup", "stdbuf", "-oL", "-eL" ,"./CypressUSB/cypress-usb-i2c-bridge/cy3240_i2c", ">", "./psocJson.txt","2>&1", "&"])

print("Starting PSOC Reader")

time.sleep(5)

ser = serial.Serial('/dev/ttyACM1', 9600)
try:
	ser.readline()
except:
	ser = serial.Serial('/dev/ttyACM0', 9600)
	

jsonTxt = ""
psocJson = ""

avgMoisture = 0
avgMotion = 0
avgLight = 0
avgHumidity = 0
avgTemp = 0

totalCount = 0
totalMoisture = 0
totalLight = 0
totalHumidity = 0
totalTemp = 0
totalMotion = 0
endMotion = 1
moisture = 0

psocJson = json.loads("{}")
alexaJson = json.loads("{}")

#Point to the PubHub Device
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-6857369c-fc38-11e6-8240-0619f8945a4f"
pnconfig.publish_key = "pub-c-c65d2091-605d-42ce-87db-8d942e2773cf"
pnconfig.ssl

pubnub = PubNub(pnconfig)

#Set user's channel to their sessionID
#channel = raw_input('Please Enter your session ID: ')
channel = "my_device" #UNCOMMENT IF YOU ARE HOSTING YOURSELF

class subCallback(SubscribeCallback):
	def message(self, pubnub, message):
		type = message['type']
		command = message['command']
		print(command)
		if type == "water":
        	        ser.write('0')

	def status(self, pubnub, status):
		if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
			print("DISCONNECTED")

		if status.category == PNStatusCategory.PNConnectedCategory:
			print("CONNECTED")

		if status.category == PNStatusCategory.PNReconnectedCategory:
			print("RECONNECTED")

		if status.category == PNStatusCategory.PNDecryptionErrorCategory:
			print("ERROR")

	def presence(self, pubnub, status):
		pass

pubnub.add_listener(subCallback())
pubnub.subscribe().channels(channel+"A").execute()

def takePhoto():
	c= subprocess.check_output(["vcgencmd","get_camera"])
	int(c.strip()[-1])
	if (c):
		print("detected")
		
	else:
		print ("not detected")

def publishDataToPubnub():
	print ("publish  function")
	takePhoto()
	if totalCount > 0:
		avgMotion = totalMotion
		avgTemp = round(totalTemp/totalCount,2)
		avgHumidity = round(totalHumidity/totalCount,2)
		avgLight = round(totalLight/totalCount,0)
		avgMoisture = round(float(totalMoisture)/totalCount,0)
		alexaJsonTxt = '{"averages":[{"timesMotionDetected":'+str(avgMotion)+', "averageTemp":'+str(avgTemp)+', "averageHumidity":'+str(avgHumidity)+', "averageLight":'+str(avgLight)+', "averageMoisture":'+str(avgMoisture)+'}],"current":[{"currentTemp":'+str(psocJson["temperature"])+', "currentHumidity":'+str(psocJson["humidity"])+', "currentLight":'+str(psocJson["illuminance"])+', "currentMoisture":'+str(moisture)+'}]}'
		alexaJson = json.loads(alexaJsonTxt)
		pubnub.publish().channel(channel+"B").message(alexaJson).should_store(True)
		print(alexaJson)	
	
	threading.Timer(10.0, publishDataToPubnub).start()

publishDataToPubnub()

while (1==1):
	fileHandle = open('psocJson.txt')
	jsonTxt = fileHandle.readlines()
	fileHandle.close()
	psocJson = json.loads(jsonTxt[-1])
	#print("working")
	if psocJson["motion"] == 1:
		endMotion = 0
	if psocJson["motion"] == 0:
		if endMotion == 0:
			endMotion = 1
			totalMotion = totalMotion + 1
	
	totalTemp = totalTemp + psocJson["temperature"]
	totalHumidity = totalHumidity + psocJson["humidity"]
	totalLight = totalLight + psocJson["illuminance"]
	totalCount = totalCount + 1
	try:
		totalMoisture = totalMoisture + float(str(ser.readline()).strip("b'").strip("\\r\\n"))
		moisture = float(str(ser.readline()).strip("b'").strip("\\r\\n"))
	except:
		totalMoisture = totalMoisture + 0
		print("Can't connect to Arduino")
