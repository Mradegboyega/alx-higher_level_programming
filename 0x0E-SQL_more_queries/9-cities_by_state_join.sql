-- 9-cities_by_states.sql

-- Use the provided database as a command-line argument
USE hbtn_0d_usa;

-- Query to list all cities with corresponding states
SELECT cities.id, cities.name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

