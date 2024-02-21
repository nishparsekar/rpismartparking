#!/usr/bin/python
from gpiozero import AngularServo #for servo
from time import sleep #for servo
import time
import RPi.GPIO as GPIO
import time
import os,sys
import drivers #for display
from urllib.parse import urlparse
import paho.mqtt.client as paho
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#GPIO.setup(12, GPIO.OUT)


display = drivers.Lcd()
cc = drivers.CustomCharacters(display)

'''
define pin for lcd
'''
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
delay = 1




slot1_Sensor = 29
slot2_Sensor = 31
slot3_Sensor = 36  #new change
slot4_Sensor = 35  #new change
slot5_Sensor = 22  #new change sensor for gate in
slot6_Sensor = 24 # new change sensor for gate out


#GPIO.setup(12, GPIO.OUT)
GPIO.setup(slot1_Sensor, GPIO.IN) 
GPIO.setup(slot2_Sensor, GPIO.IN) 
GPIO.setup(slot3_Sensor, GPIO.IN) #new change
GPIO.setup(slot4_Sensor, GPIO.IN) #new change
GPIO.setup(slot5_Sensor, GPIO.IN) #new change gate sensor
GPIO.setup(slot6_Sensor, GPIO.IN) #new change gate sensor




                  

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)# servo

#pwm=GPIO.PWM(12, 50)
#pwm.start(0)

  


def on_connect(self, mosq, obj, rc):
        self.subscribe("Fan", 0)
    
def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

mqttc = paho.Client()                        # object declaration
# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://test.mosquitto.org:1883') 
url = urlparse(url_str)
mqttc.connect(url.hostname, url.port)

    
def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(12, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(12, False)
	pwm.ChangeDutyCycle(0)
	
  


while 1:
  
  # Print out results
  rc = mqttc.loop()
  slot1_status = GPIO.input(slot1_Sensor)
  time.sleep(0.2)
  slot2_status = GPIO.input(slot2_Sensor)
  time.sleep(0.2)
  slot3_status = GPIO.input(slot3_Sensor) #new change
  time.sleep(0.2)
  slot4_status = GPIO.input(slot4_Sensor) #new change
  time.sleep(0.2)
  slot5_status = GPIO.input(slot5_Sensor) #new change
  time.sleep(0.2)
  slot6_status = GPIO.input(slot6_Sensor) #new change
  time.sleep(0.2)
  
  if (slot1_status == False):
    # Custom caracter #6. Code {0x05}.
   display.lcd_clear()
   display.lcd_display_string("S1 Parked", 1)
   mqttc.publish("slot1","1")
   time.sleep(0.2)
  else:
    #display.lcd_clear()
    display.lcd_display_string("S1 Free  ", 1)
    mqttc.publish("slot1","0")
    time.sleep(0.2)
    
  if (slot2_status == False):
   #display.lcd_clear()
   display.lcd_display_string("S2 Parked", 2)
   mqttc.publish("slot2","1")
   time.sleep(2)
  else:
    #display.lcd_clear()
    display.lcd_display_string("S2 Free  ", 2)
    mqttc.publish("slot2","0")
    time.sleep(2)

  if (slot3_status == False):
   #display.lcd_clear()
   display.lcd_display_string("S3 Parked", 1)
   mqttc.publish("slot3","1")
   time.sleep(0.2)
  else:
    #display.lcd_clear()
    display.lcd_display_string("S3 Free  ", 1)
    mqttc.publish("slot3","0")
    time.sleep(0.2)

  if (slot4_status == False):
   #display.lcd_clear()
   display.lcd_display_string("S4 Parked", 2)
   mqttc.publish("slot4","1")
   time.sleep(0.2)
  else:
    #display.lcd_clear()
    display.lcd_display_string("S4 Free  ", 2)
    mqttc.publish("slot4","0")
    time.sleep(0.2) 
    
         # for servo
  if (slot5_status == False):
   mqttc.publish("slot5","1")
   servo.angle = 90
   sleep(3)
   servo.angle = -90
   time.sleep(0.2)
  else:
    mqttc.publish("slot5","0")
    time.sleep(0.2) 

  if (slot6_status == False):
   mqttc.publish("slot6","1")
   servo.angle = 90
   sleep(3)
   servo.angle = -90
   time.sleep(0.2)
  else:
    mqttc.publish("slot6","0")
    time.sleep(0.2) 
    print ("loop end")    
    
    
    #display.lcd_clear()

    

    
    
    
  
     
   
    
    
    print ("Start")
    
        
