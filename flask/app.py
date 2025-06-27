from flask import Flask, request, jsonify
from pytoniq_core import Address

app = Flask(__name__)

@app.route('/')
def home():
    return 'TON Address Converter is running.'

@app.route('/convert', methods=['POST'])
def convert_address():
    try:
        data = request.get_json()
        raw_address = data.get('raw')
        if not raw_address:
            return jsonify({'error': 'Missing address'}), 400

        address = Address(raw_address)
        friendly = address.to_str(bounceable=True, url_safe=True)

        return jsonify({'friendly': friendly})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
