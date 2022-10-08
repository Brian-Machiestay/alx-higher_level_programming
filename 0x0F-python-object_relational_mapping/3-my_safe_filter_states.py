#!/usr/bin/python3
""" values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db_name = argv[3]
    u_pass = argv[2]
    usr = argv[1]
    arg = argv[4]

    query = "SELECT * FROM states WHERE name LIKE BINARY %s" + \
        " ORDER BY states.id"
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=u_pass,
        db=db_name,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute(query, (arg,))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
