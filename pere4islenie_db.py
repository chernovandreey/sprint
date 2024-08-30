from multiprocessing import connection

from sqlalchemy import create_engine
import psycopg2


engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432")
engine.connect()


connection = psycopg2.connect(
    user="postgres",
    password="1234",
    host="localhost",
    port="5432")

cursor = connection.cursor()

cursor.execute("SELECT datname FROM pg_database;")
databases = cursor.fetchall()
for db in databases:
    print(db[0])

cursor.close()
connection.close()
