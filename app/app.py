import sqlite3
import subprocess
import hvac
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_secrets():
    vault_addr = os.environ.get('VAULT_ADDR', 'http://127.0.0.1:8200')
    vault_token = os.environ.get('VAULT_TOKEN', 'dev-root-token')

    client = hvac.Client(url=vault_addr, token=vault_token)

    if not client.is_authenticated():
        raise Exception("Vault authentication failed")

    secret = client.secrets.kv.v2.read_secret_version(
        path='devsecops-app'
    )
    return secret['data']['data']

secrets = get_secrets()
SECRET_KEY = secrets['secret_key']
DB_PASSWORD = secrets['db_password']

app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return jsonify(cursor.fetchall())

@app.route('/ping')
def ping():
    host = request.args.get('host')
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True)
    return result.stdout.decode()

@app.route('/health')
def health():
    return jsonify({"status": "ok", "secrets_from_vault": True})

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')
