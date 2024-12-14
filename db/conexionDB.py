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
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios ( id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE NOT NULL, password VARCHAR(50) NOT NULL)")
    cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes ( id SERIAL PRIMARY KEY, nombre VARCHAR(100) NOT NULL ) ''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS ventas ( id SERIAL PRIMARY KEY, cliente_id INTEGER REFERENCES clientes(id), monto DECIMAL NOT NULL ) ''')
    cursor.execute(sql.SQL(""" INSERT INTO usuarios (username, password) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING """), ("admin", "admin"))
    conn.commit()
    conn.close()