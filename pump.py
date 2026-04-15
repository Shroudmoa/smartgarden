from gpiozero import OutputDevice
from time import sleep

def activate_pump():
    pump = OutputDevice(7)
    pump.on()
    sleep(15)  # Pumpe für 2 Sekunden aktiv
    pump.off()
activate_pump()