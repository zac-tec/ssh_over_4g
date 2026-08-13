from flask import Blueprint, jsonify
from sensor.relay import relay_on, relay_off

# create blueprint
relay_api = Blueprint("relay_api", __name__)

# ---- RELAY ON ----
@relay_api.route("/relay/on", methods=["GET"])
def relay_turn_on():
    relay_on()
    return jsonify({"status": "on"})


# ---- RELAY OFF ----
@relay_api.route("/relay/off", methods=["GET"])
def relay_turn_off():
    relay_off()
    return jsonify({"status": "off"})
