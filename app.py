from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Server is running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print('Webhook received:', data)
    return jsonify({'status': 'success', 'received': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
