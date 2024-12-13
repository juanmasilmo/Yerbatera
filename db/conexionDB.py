import psycopg2
from psycopg2 import sql

def connect_DB():
    conn=psycopg2.connect(
        host="localhost",
        database="YerbateraDB",
        user="postgres",
        password="postgres"
    )
    cursor = conn.cursor()
    