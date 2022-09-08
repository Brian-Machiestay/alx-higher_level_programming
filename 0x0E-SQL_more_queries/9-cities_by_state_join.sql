-- lists all cities contained in the database hbtn_0d_usa
SELECT DISTINCT states.id, cities.name, states.name
FROM cities, states
WHERE cities.id = state_id
ORDER BY states.id
