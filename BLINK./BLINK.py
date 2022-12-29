#For_RASPBERRY PI PICO
from machine import Pin
import utime
led=Pin(25,Pin.OUT)
led.on()
sleep(10ms)
led.off()


#For RaspBerry Pi PICO W
from machine import Pin
import utime
led=Pin("LED",Pin.OUT)
led.on()
sleep(10ms)
led.off()
