-- Task 16: List all records with a name value in the table second_table
-- SQL Query:
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

