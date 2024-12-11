-- Create the patient_db database (if it doesn't already exist)
CREATE DATABASE patient_db;

-- Connect to the patient_db database
\c patient_db

-- Create the patients table
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    medical_history TEXT,
    prescriptions TEXT,
    lab_results TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample Data (Optional)
INSERT INTO patients (name, date_of_birth, medical_history, prescriptions, lab_results)
VALUES 
    ('John Doe', '1980-05-15', 'Hypertension', 'Medication A', 'Blood test normal'),
    ('Jane Smith', '1990-10-22', 'Diabetes', 'Medication B', 'Blood sugar levels high');
