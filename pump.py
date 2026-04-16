from gpiozero import OutputDevice
from time import sleep
from my_logging import log_error

def activate_pump():
    pump = OutputDevice(7)
    try:
        pump.on()
        log_error(sensor="Pumpe", level="Info", errormsg="Pumpe aktiviert")
        sleep(15)
    finally:
        pump.off()
        log_error(sensor="Pumpe", level="Info", errormsg="Pumpe deaktiviert")