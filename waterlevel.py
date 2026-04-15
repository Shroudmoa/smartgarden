###### Adresse check mit => i2cdetect -y 1

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
                #raw data
                print("Raw data:", daten)

                # one
                wert = berechne_wert(daten)

                
                print("Wert:", wert)

                # not needed
                if wert >= 150:
                    print("Wasserstand HOCH")
                else:
                    print("Wasserstand NIEDRIG")

                print("---------------------------")

            return((wert*100)/250)

