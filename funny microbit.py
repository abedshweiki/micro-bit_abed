#abedshweiki for fun



from microbit import *

while True:
    if pin_logo.is_touched():
        display.scroll('hi the temperature is')
        display.scroll(temperature())
        display.scroll




