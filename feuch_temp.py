import adafruit_dht
import board
import time
from my_logging import log_error

# D0 = GPIO22
Temperature_Humidity_Sensor = adafruit_dht.DHT22(board.D22)

def read_temperature():
    try:
        temperature_celsius = Temperature_Humidity_Sensor.temperature
        log_error(sensor="DHT22", level="Info", errormsg=f"Temperature: {temperature_celsius}")
        return temperature_celsius

    except RuntimeError as error:
        log_error(sensor="DHT22", level="ERROR", errormsg=f"Temp read failed: {error}")
        return None


def read_humidity():
    try:
        humidity = Temperature_Humidity_Sensor.humidity
        log_error(sensor="DHT22", level="Info", errormsg=f"Humidity: {humidity}")
        return humidity

    except RuntimeError as error:
        log_error(sensor="DHT22", level="ERROR", errormsg=f"Humidity read failed: {error}")
        return None