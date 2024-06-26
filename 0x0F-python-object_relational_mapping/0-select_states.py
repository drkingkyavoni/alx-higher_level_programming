#!/usr/bin/python3

"""
Function lists all states in asc order
Return: None
"""

import sys

import MySQLdb

if __name__ == "__main__":
    """
    print states from db
    """

    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306,
        charset="utf8",
    )

    cursor = conn.cursor()
    cursor.execute("select * from states order by id asc")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    conn.close()
