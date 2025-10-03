from gpiozero import PWMLED
import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
led = PWMLED(4)

while True:
    led.value = GPIO.LOW
    time.sleep((random.randint(2000, 8000)) / 1000)

    led.value = GPIO.HIGH
    timer = 0
    while GPIO.input(17) == GPIO.HIGH:
        time.sleep(0.001)
        timer += 0.001

    print(f'Vous avez pris {timer:.3f} secondes pour reagir.')