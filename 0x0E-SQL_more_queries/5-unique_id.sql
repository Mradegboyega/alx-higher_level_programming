-- 5-unique_id.sql

-- Create table unique_id if not exists
USE hbtn_0d_2;

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

