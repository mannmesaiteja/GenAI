from dotenv import load_dotenv
import os

load_dotenv(".env")


import mysql.connector as mc

def db_connection():
    return mc.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


 # check if connection is successful or not
try:
    print(db_connection().is_connected()) # prints true if connection is successful
except Exception as e:
    print("connection failed:", str(e))