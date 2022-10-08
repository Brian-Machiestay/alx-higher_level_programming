#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa """
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db_name = argv[3]
    u_pass = argv[2]
    usr = argv[1]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=u_pass,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, "
                + "states.name FROM cities JOIN states "
                + "ON states.id = state_id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
