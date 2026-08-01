-- File: init.sql -- Author: Lex Albrandt -- Initial schema for medical device database

CREATE TABLE IF NOT EXISTS telemetry (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL,
    patient_id VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    heart_rate INTEGER,
    spo2 INTEGER,
    systolic_bp INTEGER,
    diastolic_bp INTEGER
);