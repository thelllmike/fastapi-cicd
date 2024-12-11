import time
import psycopg2
import requests
import os
from datetime import datetime

# Configuration
PATIENT_SERVICE_URL = os.getenv("PATIENT_SERVICE_URL", "http://patient-service")
APPOINTMENT_SERVICE_URL = os.getenv("APPOINTMENT_SERVICE_URL", "http://appointment-service")
REDSHIFT_DB_CONFIG = {
    "dbname": os.getenv("REDSHIFT_DB_NAME", "healthsync_db"),
    "user": os.getenv("REDSHIFT_USER", "your_user"),
    "password": os.getenv("REDSHIFT_PASSWORD", "your_password"),
    "host": os.getenv("REDSHIFT_HOST", "your-redshift-endpoint"),
    "port": os.getenv("REDSHIFT_PORT", "5439"),
}

def fetch_patients():
    try:
        response = requests.get(f"{PATIENT_SERVICE_URL}/patients")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching patients: {e}")
        return []

def fetch_appointments():
    try:
        response = requests.get(f"{APPOINTMENT_SERVICE_URL}/appointments")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching appointments: {e}")
        return []

def aggregate_data():
    patients = fetch_patients()
    appointments = fetch_appointments()

    total_patients = len(patients)
    total_appointments = len(appointments)

    print(f"Total Patients: {total_patients}")
    print(f"Total Appointments: {total_appointments}")

    # Insert aggregated data into Redshift
    try:
        conn = psycopg2.connect(**REDSHIFT_DB_CONFIG)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO aggregated_data (metric, value, timestamp) VALUES (%s, %s, %s)",
            ("total_patients", total_patients, datetime.now())
        )
        cur.execute(
            "INSERT INTO aggregated_data (metric, value, timestamp) VALUES (%s, %s, %s)",
            ("total_appointments", total_appointments, datetime.now())
        )

        conn.commit()
        cur.close()
        conn.close()
        print("Data aggregated and pushed to Redshift successfully.")
    except Exception as e:
        print(f"Error pushing data to Redshift: {e}")

if __name__ == "__main__":
    while True:
        aggregate_data()
        time.sleep(3600)  # Run every hour
