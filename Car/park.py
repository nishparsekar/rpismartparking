import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Majhe x number of sensor ahet (assuming 5 sensors on pins 4,5,6,7,8 respectively)
ir_pins = [29,31,36,35] # 29 31 36 35

 # Mala na server motor control karaychi ahe (assuming low volt servo motor connected on pin 12, use relays for high power motor)
servo_pin = 12

# IR sensors madhun input
for pin in ir_pins:
    GPIO.setup(pin, GPIO.IN)

# Servo motor/relay la output
GPIO.setup(servo_pin, GPIO.OUT)

# Saglya sensor cha input check karaychay
while True:
    ir_input = [GPIO.input(pin) for pin in ir_pins]
    if all(ir_input):
        # Jar sagle IR sensors high astil at same time tar motor work nahi karnar
        time.sleep(0.1)
    elif any(ir_input):
        # If input is high motor work karel and sleep after specified seconds (assuming specified seconds as 10)
        GPIO.output(servo_pin, GPIO.HIGH)
        time.sleep(10)
        GPIO.output(servo_pin, GPIO.LOW)
    else:
        time.sleep(0.1)