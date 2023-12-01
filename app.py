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


'''before initiate any of API, we Should to check if the user Id is correct or not, and in this case we don't have 
any authentication methods, So I will make the variable UserID = 1 and then check for each API request if the user is 
Authorized to initiate the API or not'''

UserID = 1

# To Add a new Post We should create new user.
@app.route('/user', methods=['POST'])
def create_user():
    conn = db_connection()
    cursor = conn.cursor()
    new_user = request.json
    try:
        sql = """INSERT INTO User (UserName, Email) VALUES (%s, %s)"""
        cursor.execute(sql, (new_user['UserName'], new_user['Email']))
        conn.commit()
        return f"User with id: {cursor.lastrowid} created successfully", 201
    except Exception as e:
        return str(e)

# Endpoint to add new post
@app.route('/add_post', methods=['POST'])
def add_post():
    conn = db_connection()
    cursor = conn.cursor()
    new_post = request.json
    try:
        if new_post["UserID"] == UserID:
            sql = """INSERT INTO Post (UserID, Content) VALUES (%s, %s)"""
            cursor.execute(sql, (new_post['UserID'], new_post['Content']))
            conn.commit()
            return f"Post with id: {cursor.lastrowid} created successfully", 201
        else:
            return "The User Not Found!!"
    except Exception as e:
        return str(e)

# Endpoint to update post
@app.route('/update_post', methods=['POST'])
def update_post():
    conn = db_connection()
    cursor = conn.cursor()
    post = request.json
    try:
        if post["UserID"] == UserID:
            sql = """UPDATE Post SET Content = %s WHERE PostID = %s"""
            cursor.execute(sql, (post['Content'], post['PostID']))
            conn.commit()
            return f"Post with id: {post['PostID']} updated successfully", 200
        else:
            return "The User Not Found!!"
    except Exception as e:
        return str(e)

# Endpoint to delete post
@app.route('/delete_post', methods=['POST'])
def delete_post():
    conn = db_connection()
    cursor = conn.cursor()
    post = request.json
    try:
        if post["UserID"] == UserID:
            sql = """DELETE FROM Post WHERE PostID = %s"""
            cursor.execute(sql, (post["PostID"],))
            conn.commit()
            return f"Post with id: {post['PostID']} deleted successfully", 200
        else:
            return "The User Not Found!!"
    except Exception as e:
        return str(e)

# Endpoint to get post
@app.route('/get_post', methods=['POST'])
def get_post():
    conn = db_connection()
    cursor = conn.cursor()
    post = request.json
    try:
        if post["UserID"] == UserID:
            cursor.execute("SELECT * FROM Post WHERE PostID = %s", (post["PostID"],))
            post = cursor.fetchone()
            post = dict(zip(cursor.column_names, post))
            post['Timestamp'] = post['Timestamp'].isoformat()
            return jsonify(post), 200
        else:
            return "The User Not Found!!"
    except Exception as e:
        return str(e)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
