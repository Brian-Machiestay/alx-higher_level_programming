-- lists all cities contained in the database hbtn_0d_usa
SELECT states.id, cities.name, states.name
FROM states JOIN cities
ORDER BY cities.id
