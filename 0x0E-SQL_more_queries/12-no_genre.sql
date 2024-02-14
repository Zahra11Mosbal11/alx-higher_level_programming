-- Import the database dump from hbtn_0d_tvshows
-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title ASC, tv_show_genres.genre_id ASC; 
