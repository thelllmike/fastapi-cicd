from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'patient_db'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password'),
        host=os.getenv('DB_HOST', 'localhost'),
        port='5432'
    )
    return conn

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO patients (name, date_of_birth, medical_history) VALUES (%s, %s, %s)",
        (data['name'], data['date_of_birth'], data['medical_history'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Patient added successfully"}), 201

@app.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients WHERE id = %s", (id,))
    patient = cur.fetchone()
    cur.close()
    conn.close()
    if patient:
        return jsonify({
            "id": patient[0],
            "name": patient[1],
            "date_of_birth": patient[2],
            "medical_history": patient[3]
        })
    return jsonify({"error": "Patient not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
