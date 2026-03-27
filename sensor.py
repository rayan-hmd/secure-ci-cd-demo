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
    systems = ["RADAR", "SONAR", "COMMS"]
    statuses = ["OK", "WARNING", "ERROR"]
    while True:
        # Random number of events per cycle: 1–3
        num_events = random.randint(1, 3)
        
        for _ in range(num_events):
            system = random.choice(systems)
            status = random.choice(statuses)
            
            # Determine severity
            if status == "OK":
                severity = "INFO"
            elif status == "WARNING":
                severity = "WARNING"
            else:
                severity = "ERROR"
            
            timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            
            # Generate system-specific data
            if system == "RADAR":
                track_id = random.randint(100, 999)
                print(f"[{severity}] [RADAR] [{timestamp}] TrackID={track_id} Status={status}", flush=True)
            elif system == "SONAR":
                depth = random.randint(50, 500)
                print(f"[{severity}] [SONAR] [{timestamp}] Depth={depth}m Status={status}", flush=True)
            elif system == "COMMS":
                latency = random.randint(10, 300)
                print(f"[{severity}] [COMMS] [{timestamp}] Latency={latency}ms Status={status}", flush=True)
        
        time.sleep(3)  # Wait 3 seconds before next batch


# --- Run Flask in a separate thread ---
if __name__ == "__main__":
    from threading import Thread

    log_thread = Thread(target=generate_logs)
    log_thread.daemon = True
    log_thread.start()

    # Start Flask web server for health checks and disable reloader for single-process behavior in Docker
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False) # nosec B104