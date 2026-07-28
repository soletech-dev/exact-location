from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['POST'])
def receive():
    data = request.json
    print("="*50)
    print("📍 LOCATION RECEIVED:")
    print(f"Latitude: {data.get('latitude')}")
    print(f"Longitude: {data.get('longitude')}")
    print(f"Accuracy: {data.get('accuracy')}")
    print("="*50)
    return jsonify({"status": "success"})

@app.route('/')
def home():
    return "Server is running 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
