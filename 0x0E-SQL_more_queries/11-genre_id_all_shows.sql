-- shows contained in the database hbtn_0d_tvshows
SELECT title, genre_id FROM tv_show_genres,
tv_genres,tv_shows
WHERE tv_shows.id=tv_show_genres.show_id AND
tv_show_genres.genre_id=tv_genres.id
ORDER BY tv_shows.title,tv_show_genres.genre_id;
