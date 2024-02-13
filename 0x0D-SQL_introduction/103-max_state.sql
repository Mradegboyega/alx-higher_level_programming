-- Task 20: Display the max temperature of each state ordered by state name
-- SQL Query:
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

