import psycopg2
import random
import math
from datetime import datetime, timedelta


DB_CONFIG = {
    "host": "localhost",
    "database": "growbox",
    "user": "postgres",
    "password": "super",
    "port": 5432
}

TABLE_NAME = "sensor_readings"


base = {
    "temperature": 20.0,
    "humidity": 50.0,
    "soil_moisture": 40.0,
    "water_level": 10.0
}

def vary(value, amount):
    return value + random.uniform(-amount, amount)

def generate_row(timestamp):
    hour_factor = math.sin((timestamp.hour / 24) * 2 * math.pi)

    temperature = base["temperature"] + 5 * hour_factor + random.uniform(-1, 1)
    humidity = base["humidity"] - 10 * hour_factor + random.uniform(-3, 3)
    soil_moisture = base["soil_moisture"] + random.uniform(-5, 5)
    water_level = base["water_level"] + random.uniform(-0.5, 0.5)

    return (
        timestamp,
        soil_moisture,
        temperature,
        humidity,
        water_level
    )

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    now = datetime.utcnow()

    total_points = 48 

    start_time = now - timedelta(hours=24)
    step = timedelta(seconds=(24 * 60 * 60) / total_points)

    for i in range(total_points):
        ts = start_time + (step * i)
        row = generate_row(ts)

        cur.execute(f"""
            INSERT INTO {TABLE_NAME}
            (timestamp, soil_moisture, temperature, humidity, water_level)
            VALUES (%s, %s, %s, %s, %s)
        """, row)

    conn.commit()
    cur.close()
    conn.close()

    print(f"Inserted {total_points} fake rows over 24h ")

if __name__ == "__main__":
    main()