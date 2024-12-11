from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def send_notification():
    data = request.json
    message = f"Reminder: {data['message']}"
    print(message)
    return jsonify({"message": "Notification sent"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
