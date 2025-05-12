import mysql.connector
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="aadhar_app"
    )

def insert_user_data(name, dob, aadhar, filename):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO user_data (name, dob, aadhar_number, upload_filename)
            VALUES (%s, %s, %s, %s)
        """, (name, dob, aadhar, filename))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
