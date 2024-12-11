from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'appointment_db'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password'),
        host=os.getenv('DB_HOST', 'localhost'),
        port='5432'
    )
    return conn

@app.route('/appointments', methods=['POST'])
def schedule_appointment():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO appointments (patient_id, doctor_name, appointment_date) VALUES (%s, %s, %s)",
        (data['patient_id'], data['doctor_name'], data['appointment_date'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Appointment scheduled successfully"}), 201

@app.route('/appointments', methods=['GET'])
def list_appointments():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM appointments")
    appointments = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {
            "id": appt[0],
            "patient_id": appt[1],
            "doctor_name": appt[2],
            "appointment_date": appt[3]
        } for appt in appointments
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
