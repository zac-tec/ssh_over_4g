from flask import Blueprint, jsonify
from sensor.dht import read_sensor
import time
import subprocess

api = Blueprint("api", __name__)


# ---------------- SENSOR DATA API ----------------
@api.route("/data")
def data():
    temp, hum = read_sensor()

    return jsonify({
        "temperature": temp,
        "humidity": hum,
        "time": int(time.time())
    })


# ---------------- PI HEALTH FUNCTION ----------------
def get_pi_health():
    return {
        "cpu_temp": subprocess.getoutput(
            "vcgencmd measure_temp"
        ).replace("temp=", ""),

        "cpu_usage": subprocess.getoutput(
            "top -bn1 | grep 'Cpu(s)' | awk '{print 100-$8}'"
        ) + " %",

        "ram": subprocess.getoutput(
            "free -h | awk '/Mem:/ {print $3\" / \"$2}'"
        ),

        "disk": subprocess.getoutput(
            "df -h / | awk 'NR==2 {print $4}'"
        ),

        "uptime": subprocess.getoutput("uptime -p"),

        "ip": subprocess.getoutput("hostname -I").split()[0]
    }


# ---------------- PI HEALTH API ----------------
@api.route("/health")
def health():
    return jsonify(get_pi_health())
