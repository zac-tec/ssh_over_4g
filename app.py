from flask import Flask, render_template, jsonify
from routes.api import api
from routes.relay import relay_api
import time

app = Flask(__name__)

# ---------------- SETTINGS ----------------
# Auto reload HTML when edited (useful during development)
app.config["TEMPLATES_AUTO_RELOAD"] = True


# ---------------- REGISTER BLUEPRINTS ----------------
app.register_blueprint(api)
app.register_blueprint(relay_api)


# ---------------- DASHBOARD ROUTE ----------------
@app.route("/")
def home():
    return render_template("dashboard.html")


# ---------------- STATUS CHECK API (NEW) ----------------
# Used to verify server is alive
@app.route("/status")
def status():
    return jsonify({
        "status": "online",
        "timestamp": int(time.time())
    })


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",   # allow phone access
        port=5000,
        debug=False,
        use_reloader=False
    )
