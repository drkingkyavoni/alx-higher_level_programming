#!/usr/bin/python3

"""
Function that filters state with names that start with 'N'
Returns: None
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    filters state with names that start with 'N'
    from a db table with username and password
    """

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )

    cursor = conn.cursor()
    results = cursor.execute(
        "select * from states where name like 'N%' order by id asc"
    ).fetchall()

    for row in results:
        print(row)
    cursor.close()
    conn.close()
