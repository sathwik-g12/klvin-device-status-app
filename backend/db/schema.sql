-- Drop old tables if they exist (safe re-run)
DROP TABLE IF EXISTS device_readings, devices, companies CASCADE;

-- 1️ Companies Table
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- 2️ Devices Table
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL
);

-- 3️ Device Readings Table
CREATE TABLE device_readings (
    id SERIAL PRIMARY KEY,
    device_id INT REFERENCES devices(id) ON DELETE CASCADE,
    reading_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample companies
INSERT INTO companies (name) VALUES
('Alpha Tech'),
('Beta Innovations'),
('Gamma Systems');

-- Insert some sample devices for each company
INSERT INTO devices (company_id, name) VALUES
(1, 'Alpha Device 1'),
(1, 'Alpha Device 2'),
(1, 'Alpha Device 3'),
(2, 'Beta Device 1'),
(2, 'Beta Device 2'),
(3, 'Gamma Device 1'),
(3, 'Gamma Device 2'),
(3, 'Gamma Device 3');

-- Insert some sample readings to simulate online/offline status
INSERT INTO device_readings (device_id, reading_time) VALUES
(1, NOW()),
(2, NOW() - INTERVAL '3 minutes'),
(3, NOW() - INTERVAL '1 minute'),
(4, NOW()),
(5, NOW() - INTERVAL '5 minutes'),
(6, NOW()),
(7, NOW() - INTERVAL '2 minutes'),
(8, NOW() - INTERVAL '6 minutes');
