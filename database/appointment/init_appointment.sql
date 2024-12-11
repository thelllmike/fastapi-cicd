-- Create the appointment_db database (if it doesn't already exist)
CREATE DATABASE appointment_db;

-- Connect to the appointment_db database
\c appointment_db

-- Create the appointments table
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    appointment_date TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'Scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Foreign Key Constraint (if needed)
-- ALTER TABLE appointments ADD CONSTRAINT fk_patient FOREIGN KEY (patient_id) REFERENCES patients(id);

-- Sample Data (Optional)
INSERT INTO appointments (patient_id, doctor_name, appointment_date, status)
VALUES 
    (1, 'Dr. Smith', '2024-06-15 10:00:00', 'Scheduled'),
    (2, 'Dr. Johnson', '2024-06-20 14:00:00', 'Confirmed');
