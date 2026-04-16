from pitop.pma.adc_base import ADCBase
from my_logging import log_error

def read_soil_moisture(port="A0", pin_number=1):
    sensor = ADCBase(
        port_name=port,
        pin_number=pin_number,
        name="moisture_sensor",
        number_of_samples=1,
    )

    try:
        raw = sensor.read()
        if raw is None:
            log_error(sensor="Bodenfeuchte Sensor", level="ERROR", errormsg="Kein Wert")
            return None
    except Exception as e:
        log_error(sensor="Bodenfeuchte Sensor", level="ERROR", errormsg=str(e))
        return None

    moisture_percent = (raw / 750) * 100
    log_error(sensor="Boenfeuchte Sensor", level="Info", errormsg=f"Bodenfeuchte: {moisture_percent}")
    return moisture_percent