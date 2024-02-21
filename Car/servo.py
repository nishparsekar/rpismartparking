import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

ir_pins = [29, 31, 36, 35] 
ir_gate_pins= [16, 18]
servo = GPIO.PWM(12,50)

servo.start(0)
print ("Waiting for 1 second")
time.sleep(1)

print ("Rotating at intervals of 12 degrees")
duty = 2
while duty <= 17:
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1

    print ("Turning back to 0 degrees")
servo.ChangeDutyCycle(2)
time.sleep(1)
servo.ChangeDutyCycle(0)

servo.stop()
GPIO.cleanup()
print ("Everything's cleaned up")