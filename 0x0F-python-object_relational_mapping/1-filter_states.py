#!/usr/bin/python3
""" ists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    usr = argv[1]
    usr_pss = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=usr_pss,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE"
                + "(name) LIKE BINARY 'N%' ORDER BY states.id")

    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
