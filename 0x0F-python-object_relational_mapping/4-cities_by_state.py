#!/usr/bin/python3

"""
    Module contains get_city_by_state function
    Returns: None
"""

import sys

import MySQLdb


if __name__ == "__main__":
    """
    Function lists all cities with states
    from a db table with username and password
    """

    if len(sys.argv) != 4:
        sys.exit(1)

    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306,
        charset="utf8",
    )

    cursor = conn.cursor()

    cursor.execute(
        "select cities.id, cities.name, states.name from cities join states on states.id = cities.state_id order by cities.id asc"
    )

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()


