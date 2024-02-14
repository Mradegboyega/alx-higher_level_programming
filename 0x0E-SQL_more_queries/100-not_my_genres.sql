-- 17-not_my_genre.sql

-- Use the provided database directly
USE hbtn_0d_tvshows;

-- Temporary table to store genres linked to Dexter
CREATE TEMPORARY TABLE dexter_genres AS
SELECT tv_genres.id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter';

-- Query to list genres not linked to Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN dexter_genres ON tv_genres.id = dexter_genres.id
WHERE dexter_genres.id IS NULL
ORDER BY tv_genres.name ASC;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS dexter_genres;

