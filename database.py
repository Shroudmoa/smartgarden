import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="growbox",
        user="postgres",
        password="super"
    )

conn = get_connection()
conn.autocommit = True
cur = conn.cursor()

def insert_readings(soil, temp, humidity, water):
    cur.execute(
        """
        INSERT INTO sensor_readings (
            soil_moisture,
            temperature,
            humidity,
            water_level
        ) VALUES (%s, %s, %s, %s)
        """,
        (soil, temp, humidity, water)
    )