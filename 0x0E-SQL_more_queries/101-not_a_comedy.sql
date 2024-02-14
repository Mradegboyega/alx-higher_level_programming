-- 18-no_comedy_tonight.sql

-- Use the provided database directly
USE hbtn_0d_tvshows;

-- Temporary table to store shows with the genre Comedy
CREATE TEMPORARY TABLE comedy_shows AS
SELECT tv_shows.id
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy';

-- Query to list shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN comedy_shows ON tv_shows.id = comedy_shows.id
WHERE comedy_shows.id IS NULL
ORDER BY tv_shows.title ASC;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS comedy_shows;

