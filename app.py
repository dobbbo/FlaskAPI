import os
import psycopg2
from datetime import datetime, timezone
from dotenv import load_dotenv
from flask import Flask, request

CREATE_STATIONS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stations (id SERIAL PRIMARY KEY, name TEXT);"
)

CREATE_PRICES_TABLE = """CREATE TABLE IF NOT EXISTS prices (station_id INTEGER, price REAL, date TIMESTAMP, FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE);"""

INSERT_STATION_RETURN_ID = "INSERT INTO stations (name) VALUES (%s) RETURNING id;"

INSERT_PRICE = (
    "INSERT INTO prices (station_id, price, date) VALUES (%s, %s, %s);"
)

NUMBER_OF_DAYS = (
    """SELECT COUNT(DISTINCT DATE(date)) AS days FROM prices;"""
)

AVERAGE_PRICE = """SELECT AVG(price) as average FROM prices;"""

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.post("/api/station")
def create_station():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_STATIONS_TABLE)
            cursor.execute(INSERT_STATION_RETURN_ID, (name,))
            station_id = cursor.fetchone()[0]
    return {"id": station_id, "message": f"{name} petrol station created."}, 201

@app.post("/api/price")
def add_price():
    data = request.get_json()
    price = data["price"]
    station_id = data["station"]
    try:
        date = datetime.strptime(data["date"], "%d-%m-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_PRICES_TABLE)
            cursor.execute(INSERT_PRICE, (station_id, price, date))
    
    return {"message": "Petrol price added."}, 201

@app.get("/api/average")
def get_average_price():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(AVERAGE_PRICE)
            average = cursor.fetchone()[0]
            cursor.execute(NUMBER_OF_DAYS)
            days = cursor.fetchone()[0]
    return {"average": round(average, 2), "days": days}