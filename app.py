from flask import Flask, request
import subprocess
import re
import ipaddress

app = Flask(__name__)

def is_safe_host(host):
    if not host:
        return False
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        pass

    # Conservative hostname validation (labels 1-63 chars, alnum/hyphen, no leading/trailing hyphen)
    hostname_pattern = re.compile(
        r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*$"
    )
    return bool(hostname_pattern.fullmatch(host))

@app.route('/ping')
def ping():
    host = request.args.get('host')

    if not is_safe_host(host):
        return "Invalid host", 400

    subprocess.run(["ping", "-c", "1", host], check=False, capture_output=True, text=True)

    return "Ping completed"

app.run(host="0.0.0.0", port=5000)
