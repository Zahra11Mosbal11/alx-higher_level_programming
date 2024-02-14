-- Import the database hbtn_0d_tvshows_rate
-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, tv_show_ratings.rating FROM tv_shows
OIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
ORDER BY tv_show_ratings.rating DESC;