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
    print("Starting Flask server...")
    print("Access the map at: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
