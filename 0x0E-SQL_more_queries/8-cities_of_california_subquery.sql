-- 8-cities_of_california_subquery.sql

-- Use the provided database as a command-line argument
USE hbtn_0d_usa;

-- Query to list all cities of California using a subquery
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

