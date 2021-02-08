from gpiozero import PWMLED
from signal import pause

red = PWMLED(17)

red.pulse()

pause()