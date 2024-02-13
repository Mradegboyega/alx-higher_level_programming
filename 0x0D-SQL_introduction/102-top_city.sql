-- Task 19: Display the top 3 cities' temperatures during July and August ordered by temperature (descending)
-- SQL Query:
SELECT city, ROUND(AVG(value), 4) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

