import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

motor_1a = 7
motor_1b = 11
motor_1e = 15

motor_2a = 10
motor_2b = 8
motor_2e = 12

motor_3a = 19
motor_3b = 21
motor_3e = 23

GPIO.setup(motor_1a, GPIO.OUT)
GPIO.setup(motor_1b, GPIO.OUT)
GPIO.setup(motor_1e, GPIO.OUT)

GPIO.setup(motor_2a, GPIO.OUT)
GPIO.setup(motor_2b, GPIO.OUT)
GPIO.setup(motor_2e, GPIO.OUT)

GPIO.setup(motor_3a, GPIO.OUT)
GPIO.setup(motor_3b, GPIO.OUT)
GPIO.setup(motor_3e, GPIO.OUT)

print('Turning Motor on! WEEEEEE.')

GPIO.output(motor_1a, GPIO.HIGH)
GPIO.output(motor_1b, GPIO.LOW)
GPIO.output(motor_1e, GPIO.HIGH)

sleep(3)
GPIO.output(motor_1e, GPIO.LOW)

GPIO.output(motor_2a, GPIO.HIGH)
GPIO.output(motor_2b, GPIO.LOW)
GPIO.output(motor_2e, GPIO.HIGH)

sleep(3)

print('Stopping motor')
GPIO.output(motor_2e, GPIO.LOW)

GPIO.output(motor_3a, GPIO.HIGH)
GPIO.output(motor_3b, GPIO.LOW)
GPIO.output(motor_3e, GPIO.HIGH)

sleep(3)

GPIO.output(motor_3e, GPIO.LOW)

GPIO.cleanup()
