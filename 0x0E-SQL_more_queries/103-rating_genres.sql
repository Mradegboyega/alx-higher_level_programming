-- 103-rating_genres.sql

-- Use the provided database directly
USE hbtn_0d_tvshows_rate;

-- Query to list genres by their rating sum
SELECT tv_genres.name, SUM(tv_show_genres.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;

