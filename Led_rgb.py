from gpiozero RGBLED
from time import sleep
#from __future__ import division

led = RGBLED(red=9, green=10, blue=11)

led.red = 1
sleep(1)
led.red = 0.5
sleep(1)

led.color = (0, 1, 0)
sleep(1)
led.color = (1, 0, 1)
sleep(1)
led.color = (1, 1, 0)
sleep(1)
led.color = (0, 1, 1)
sleep(1)
led.color = (1, 1, 1)
sleep(1)

led.color = (0, 0, 0)
sleep(1)

for n in range(100):
    led.blue = n/100
    sleep(0.1)

