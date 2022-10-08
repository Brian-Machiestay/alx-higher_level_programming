#!/usr/bin/python3
"""lists all cities of that state"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db_name = argv[3]
    u_pass = argv[2]
    usr = argv[1]
    st_nm = argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=u_pass,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities"
                + " INNER JOIN states ON states.id = state_id"
                + " WHERE states.name LIKE BINARY %s", (st_nm,))
    rows = cur.fetchall()
    length = 0
    for row in rows:
        print("{}".format(row[0],), end="")
        if length < len(rows) - 1:
            print(", ", end="")
        length = length + 1
    print()
