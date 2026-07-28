from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/data', methods=['POST'])
def receive():
  data = request.json
  print('=' * 50, flush=True)
  print('📍 EXACT LOCATION RECEIVED:', flush=True)
  print(f"Address: {data.get('address')}", flush=True)
  print(f"Lat: {data.get('latitude')}", flush=True)
  print(f"Lng: {data.get('longitude')}", flush=True)
  print(f"Accuracy: {data.get('accuracy')} meters", flush=True)
  print('=' * 50, flush=True)
  return jsonify({'status': 'success', 'received': data})


@app.route('/')
def home():
  return 'Server running 🚀'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
