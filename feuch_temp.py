import adafruit_dht
import board
import time

# D0 = GPIO22
Temperature_Humidity_Sensor = adafruit_dht.DHT22(board.D22)

def read_temperature():
    try:
        temperature_celcius = Temperature_Humidity_Sensor.temperature
        humidity = Temperature_Humidity_Sensor.humidity
        print (temperature_celcius)

        return temperature_celcius

    except RuntimeError as error:
        return None

def read_humidity():
    try:
        humidity = Temperature_Humidity_Sensor.humidity
        print (humidity)

        return humidity

    except RuntimeError as error:
        return None