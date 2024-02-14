-- 4-id_not_null.sql

-- Create table id_not_null if not exists
USE hbtn_0d_2;

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

