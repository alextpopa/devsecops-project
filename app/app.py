import sqlite3
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# VULNERABILITATE: SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return jsonify(cursor.fetchall())

# VULNERABILITATE: Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True)
    return result.stdout.decode()

# VULNERABILITATE: secret hardcodat
SECRET_KEY = "super-secret-key-1234"
DB_PASSWORD = "admin123"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
