# Establishes MySQL Connection
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DivSQL134@",
        database="online_store"
    )

    return connection