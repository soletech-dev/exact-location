from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['POST'])

def receive():
  data = request.json
  print('=' * 50, flush=True)
  print('📍 LOCATION RECEIVED:', flush=True)
  print(f"Latitude: {data.get('latitude')}", flush=True)
  print(f"Longitude: {data.get('longitude')}", flush=True)
  print(f"Accuracy: {data.get('accuracy')}", flush=True)
  print('=' * 50, flush=True)

  return jsonify({'status': 'success'})

@app.route('/')
def home():
    return "Server is running 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)