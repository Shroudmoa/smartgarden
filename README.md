Technische Dokumentation Smart Garten

Projektbeschreibung
Das Projekt Smart Garten ist ein automatisiertes System zur Überwachung und Bewässerung von Pflanzen. Ein Raspberry Pi 4 (Pi-Top4) dient als zentrale Steuereinheit. Sensoren erfassen kontinuierlich Umgebungs- und Bodenwerte und steuern eine Pumpe zur Bewässerung.

<<<<<<< HEAD
Hardware: Pi-top mit Extension Plate
=======
Hardware:
Pi-top mit Extension Plate
>>>>>>> 9a6b0a0 (second order)

Sensoren und Aktoren :

Temperatur und Luftfeuchtigkeitssensor
Grove Temperature and Humidity Sensor Pro
SKU 101020019
Webseite [https://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/](https://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/)
Anschluss D0

Bodenfeuchtesensor
Grove Moisture Sensor
SKU 101020008
Webseite [https://wiki.seeedstudio.com/Grove-Moisture_Sensor/](https://wiki.seeedstudio.com/Grove-Moisture_Sensor/)
Anschluss A0

Wasserstandsensor
Grove Water Level Sensor
SKU 101020635
Webseite [https://wiki.seeedstudio.com/Grove-Water-Level-Sensor/](https://wiki.seeedstudio.com/Grove-Water-Level-Sensor/)
Anschluss I2C

Pumpe
Peristaltikpumpe
Anschluss D4

Software
Programmiersprache Python

Struktur
main.py zentrale Steuerung des Systems

Weitere Skripte
feuch_temp.py
moist.py
wLevel.py
pumpe.py

Datenverarbeitung
Alle Sensordaten werden erfasst und in einer Datenbank gespeichert.
Die Daten werden anschließend in Grafana visualisiert und dargestellt.

Zugriff
Web Zugriff über Browser
[http://ip-adresse:8080]

Visual Studio Code im Browser zur Bearbeitung des Codes

SSH Zugriff auf das System ist möglich

Systemüberwachung
Über btop kann die Systemlast überwacht werden.
CPU und RAM Auslastung werden kontrolliert.

Funktionsweise
Die Sensoren erfassen kontinuierlich Messwerte.
Die Daten werden an Main.py übergeben und verarbeitet.
Die Werte werden in der Datenbank gespeichert.
Bei niedriger Bodenfeuchtigkeit wird die Pumpe automatisch aktiviert.
Die Daten werden in Grafana visualisiert.

Fehler
Hier werden die aufgetretenen Fehlermeldungen eingefügt.

Erweiterung
Verbesserung der automatischen Bewässerungslogik
Benachrichtigungen bei Störungen oder niedrigem Wasserstand
Mögliche mobile Anbindung des Systems
