import mysql.connector
from mysql.connector import Error

def check_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # Replace with your username
            password='Kw@8149365202',    # Replace with your password
            database='onlinebookstore'     # Replace with your database name
        )

        if connection.is_connected():
            print("Connection successful!")
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version:", db_info)

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    check_connection()
