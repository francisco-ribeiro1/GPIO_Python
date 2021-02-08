from gpiozero import PWMLED
from time import sleep

red = PWMLED(17)

while True:
    red.value = 0
    sleep(1)
    red.value = 0.5
    sleep(1)
    red.value = 1.0
    sleep(1)
    
