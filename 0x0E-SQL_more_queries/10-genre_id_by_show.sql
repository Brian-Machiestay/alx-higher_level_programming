-- shows contained in the database hbtn_0d_tvshows
SELECT title, genre_id FROM hbtn_0d_tvshows.tv_show_genres,
hbtn_0d_tvshows.tv_genres,hbtn_0d_tvshows.tv_shows
WHERE hbtn_0d_tvshows.tv_shows.id=hbtn_0d_tvshows.tv_show_genres.show_id AND
hbtn_0d_tvshows.tv_show_genres.genre_id=hbtn_0d_tvshows.tv_genres.id
ORDER BY tv_shows.title,tv_show_genres.genre_id;
