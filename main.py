import time
from database import insert_readings
from database import get_connection
from pump import activate_pump
from feuch_temp import read_humidity
from feuch_temp import read_temperature
from waterlevel import lese_wassterstand
from soil_moisture import read_soil_moisture
from my_logging import log_error


while True:
    log_error(sensor="SYSTEM", level="Info", errormsg="Loop iteration started")
    soil = read_soil_moisture()
    temp = read_temperature()
    humidity = read_humidity()
    water = lese_wassterstand()
    try:
        insert_readings(soil, temp, humidity, water)
    except Exception as e:
        log_error(sensor="DATABASE", level="ERROR", errormsg=str(e))
    if water is not None and soil is not None:
        if water >= 10 and soil < 20:
             activate_pump()
    time.sleep(60)
