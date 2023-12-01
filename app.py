from flask import Flask, request, jsonify
import mysql.connector
import json

app = Flask(__name__)


# Database connection
def db_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="crocosoft_db"
        )
    except mysql.connector.Error as e:
        print(e)
    return conn

if __name__ == '__main__':
    app.run(debug=True, port=5000)
