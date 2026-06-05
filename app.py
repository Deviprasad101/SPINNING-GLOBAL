from flask import Flask, send_from_directory
import os
import logging

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Disable default Flask/Werkzeug access logs to hide the 304/200 messages
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def index():
    # Serve the main map by default
    return send_from_directory(BASE_DIR, 'control_grid_map.html')

@app.route('/<path:path>')
def serve_file(path):
    # Serve any other files in this directory (e.g. map.html)
    return send_from_directory(BASE_DIR, path)

if __name__ == '__main__':
    # Use a less commonly occupied default port so this app does not clash with
    # other local services that often use 5000 (which can return unrelated JSON).
    port = int(os.environ.get("PORT", 5050))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"

    print("Starting Flask server...")
    print(f"Access the map at: http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
