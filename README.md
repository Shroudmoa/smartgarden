Technische Dokumentation Smart Garten

Projektbeschreibung
Das Projekt Smart Garten ist ein automatisiertes System zur Überwachung und Bewässerung von Pflanzen. Ein Raspberry Pi 4 (Pi-Top4) dient als zentrale Steuereinheit. Sensoren erfassen kontinuierlich Umgebungs- und Bodenwerte und steuern eine Pumpe zur Bewässerung.

- Programmiersprache Python

- main.py zentrale Steuerung des Systems

- Hardware: Pi-top mit Extension Plate
----------------------------------------------------------------------------
Sensoren und Aktoren :

Temperatur und Luftfeuchtigkeitssensor
Grove Temperature and Humidity Sensor Pro
<img width="335" height="300" alt="image" src="https://github.com/user-attachments/assets/52c8d2f8-00ce-4148-899d-ec27841c7652" />
SKU 101020019
Webseite [https://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/](https://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/)
Anschluss D0

Bodenfeuchtesensor
Grove Moisture Sensor
<img width="345" height="292" alt="image" src="https://github.com/user-attachments/assets/c4236477-646b-47b5-a4d6-a52ffd2fd2d9" />
SKU 101020008
Webseite [https://wiki.seeedstudio.com/Grove-Moisture_Sensor/](https://wiki.seeedstudio.com/Grove-Moisture_Sensor/)
Anschluss A0

Wasserstandsensor
Grove Water Level Sensor
<img width="335" height="300" alt="image" src="https://github.com/user-attachments/assets/463aeb59-125b-4201-bb08-dafc76ac149e" />
SKU 101020635
Webseite [https://wiki.seeedstudio.com/Grove-Water-Level-Sensor/](https://wiki.seeedstudio.com/Grove-Water-Level-Sensor/)
Anschluss I2C

Pumpe
Peristaltikpumpe
Anschluss D4

------------------------------------------------------------------




Wie erwähnt haben wir ein main.py als Hauptprogeramm, das als ein Service am laufen ist. 
sudo systemctl status main

weitere Skripte sind :
- feuch_temp.py
- soil_moisture.py
- wLevel.py
- pump.py

Datenverarbeitung
Alle Sensordaten werden erfasst und in einer Datenbank gespeichert.
Die Daten werden anschließend in Grafana visualisiert und dargestellt.

Zugriff
Web Zugriff über Browser
Visual Studio Code im Browser zur Bearbeitung des Code. Gesichert mit passwort. 
[http://ip-adresse:8080]
<img width="709" height="700" alt="image" src="https://github.com/user-attachments/assets/d6599786-4b14-4e6e-9add-71d01bc0723b" />
<img width="682" height="507" alt="image" src="https://github.com/user-attachments/assets/261ab698-fcc0-4d60-8902-f6c4deb80e68" />

Grafana zur Überwachung
[http://server-ip:3000]

Systemüberwachung
Über btop kann die Systemlast überwacht werden, wenn man per ssh auf dem pi-top zugreift. 
CPU und RAM Auslastung werden kontrolliert.
<img width="945" height="1040" alt="image" src="https://github.com/user-attachments/assets/78dce34c-edfa-47b7-bab3-1579494e74f1" />




Funktionsweise
Die Sensoren erfassen kontinuierlich Messwerte.
Die Daten werden an main.py übergeben und verarbeitet.
Die Werte werden in der Datenbank gespeichert.
Bei niedriger Bodenfeuchtigkeit wird die Pumpe automatisch aktiviert.
Die Daten werden in Grafana visualisiert.


Erweiterung in build
Discord Benachrichtigung-bot
weitere sensoren
Mögliche mobile Anbindung des Systems
