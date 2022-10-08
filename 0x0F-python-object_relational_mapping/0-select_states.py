#!/usr/bin/python3
""" this module connects to mysql database using the API"""
if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    username = argv[1]
    passwrd = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=passwrd,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
