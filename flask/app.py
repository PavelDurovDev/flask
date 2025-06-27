from flask import Flask, request, jsonify
from pytoniq_core import Address

app = Flask(__name__)

@app.route('/')
def home():
    return 'TON Address Converter is running.'

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json(force=True)
    raw = data.get('raw')
    if not raw:
        return jsonify({'error': 'Missing raw address'}), 400

    try:
        addr = Address(raw)
        friendly = addr.to_str(bounceable=True, url_safe=True)
        return jsonify({'friendly': friendly})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
