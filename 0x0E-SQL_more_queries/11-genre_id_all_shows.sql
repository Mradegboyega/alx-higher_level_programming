-- 11-genre_id_for_all_shows.sql

-- Use the provided database directly
USE hbtn_0d_tvshows;

-- Query to list all shows with their linked genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

