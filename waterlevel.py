from my_logging import log_error
from smbus2 import SMBus
import time

BUS_NUMMER = 1
ADRESSE = 0x77


def lese_sensor(bus, adresse):
    try:
        return bus.read_i2c_block_data(adresse, 0x00, 21)
    except:
        return None


def berechne_wert(daten):
    """
    21 values 0> one (0–255)
    """
    if not daten:
        return None

    wert = sum(daten) / len(daten)   # avg
    return round(wert, 2)


def lese_wassterstand():
    with SMBus(BUS_NUMMER) as bus:

        daten = lese_sensor(bus, ADRESSE)

        if daten:
            print("Raw data:", daten)
            wert = berechne_wert(daten)

            if wert >= 150:
                log_error(sensor="Wasserstandssensor", level="Info", errormsg=f"Wasserstand HOCH: {wert}")
            else:
                log_error(sensor="Wasserstandssensor", level="Info", errormsg=f"Wasserstand NIEDRIG {wert}")

            return (wert * 100) / 250

        else:
            log_error(sensor="Wasserstandssensor", level="ERROR", errormsg="Keine Daten gelesen")
            return None

