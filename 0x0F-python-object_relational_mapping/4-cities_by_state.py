#!/usr/bin/python3

import sys

import MySQLdb

"""
    Module contains get_city_by_state function
    Returns: None
"""


def get_cities_by_state(_usr: str, _pwd: str, _db: str) -> None:
    """
    Function lists all cities with states
    from a db table with username and password
    """
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=_usr, passwd=_pwd, db=_db, charset="utf8"
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


if __name__ == "__main__":
    _, _usr, _pwd, _db = tuple(sys.argv)
    get_cities_by_state(_usr, _pwd, _db)
