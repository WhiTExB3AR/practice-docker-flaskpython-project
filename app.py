import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'thuy',
                    'email': 'thuy@gmail.com',
                    'message': 'Xin chào!!!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
