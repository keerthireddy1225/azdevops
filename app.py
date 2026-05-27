from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping')
def ping():
    host = request.args.get('host')

    # Vulnerable command injection
    os.system(f"ping -c 1 {host}")

    return "Ping completed"

app.run(host="0.0.0.0", port=5000)
