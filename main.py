import time
from database import insert_readings
from database import get_connection
from pump import activate_pump
from feuch_temp import read_humidity
from feuch_temp import read_temperature
from waterlevel import lese_wassterstand
from soil_moisture import read_soil_moisture

conn = get_connection()
conn.autocommit = True
cur = conn.cursor()


while True:
    soil = read_soil_moisture()
    temp = read_temperature()
    humidity = read_humidity()
    water = lese_wassterstand()
    insert_readings(soil, temp, humidity, water)
    time.sleep(60)
    if water >= 10 and soil < 40:
         activate_pump()

