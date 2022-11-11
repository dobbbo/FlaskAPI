import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

CREATE_STATIONS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stations (id SERIAL PRIMARY KEY, name TEXT);"
)

CREATE_PRICES_TABLE = """CREATE TABLE IF NOT EXISTS prices (station_id TEXT, price REAL, date TIMESTAMP, FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE);"""

INSERT_STATION_RETURN_ID = "INSERT INTO stations (name) VALUES (%s) RETURNING id;"

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get("/")
def home():
    return "Hello, world!"