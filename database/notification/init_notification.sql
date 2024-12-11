-- Create the notification_db database (if it doesn't already exist)
CREATE DATABASE notification_db;

-- Connect to the notification_db database
\c notification_db

-- Create the notifications table
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Foreign Key Constraint (if needed)
-- ALTER TABLE notifications ADD CONSTRAINT fk_patient FOREIGN KEY (patient_id) REFERENCES patients(id);

-- Sample Data (Optional)
INSERT INTO notifications (patient_id, message)
VALUES 
    (1, 'Reminder: You have an appointment with Dr. Smith on 2024-06-15 at 10:00 AM'),
    (2, 'Reminder: Your follow-up appointment with Dr. Johnson is on 2024-06-20 at 2:00 PM');
