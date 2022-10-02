-- shows contained in the database hbtn_0d_tvshows
SELECT sh.title,genre_id
FROM tv_shows AS sh
LEFT JOIN tv_genres ON sh.id=tv_genres.id
LEFT JOIN tv_show_genres ON
sh.id=tv_show_genres.show_id
ORDER BY sh.title,tv_show_genres.genre_id;
