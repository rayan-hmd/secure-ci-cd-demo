import time
import random
from datetime import datetime
from flask import Flask, jsonify

# --- Flask app for /health endpoint ---
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "System running"}), 200

# --- Function to generate logs ---
def generate_logs():
    sensor_ids = [1, 2, 3, 4, 5]
    statuses = ["OK", "OK", "OK", "WARNING", "ERROR"]
    while True:
        sensor = random.choice(sensor_ids)
        status = random.choice(statuses)
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[SYSTEM] [{timestamp}] Sensor #{sensor}: {status}")
        time.sleep(3)

# --- Run Flask in a separate thread ---
if __name__ == "__main__":
    from threading import Thread

    log_thread = Thread(target=generate_logs)
    log_thread.daemon = True
    log_thread.start()

    # Start Flask web server for health checks
    app.run(host="0.0.0.0", port=5000)