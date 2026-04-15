from pitop.pma.adc_base import ADCBase

def read_soil_moisture(port="A0", pin_number=1):
    sensor = ADCBase(
        port_name=port,
        pin_number=pin_number,
        name="moisture_sensor",
        number_of_samples=1,
    )

    raw = sensor.read()
    print(raw)
    #Nase erde liefert werte bis 750, wir zeigen Prozent an für übersichtlichtkeit daher *100/750
    moisture_percent = (raw / 750) * 100
    return moisture_percent
