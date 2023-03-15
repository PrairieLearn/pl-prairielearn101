import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PINS = [16,12,7,8,25,24,23,18,15,14]

def setup_pins(pinList):
    for p in pinList:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)

def write_bar(pinList, k):
    for p in pinList[:k]:
        GPIO.output(p, GPIO.HIGH)
