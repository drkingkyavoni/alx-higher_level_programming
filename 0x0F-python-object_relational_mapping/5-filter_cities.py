#!/usr/bin/python3

import sys

import MySQLdb

"""
    Module contains get_city_by_state function
    Returns: None
"""


def get_filter_cities_by_state(_usr: str, _pwd: str, _db: str, _city: str) -> None:
    """
    Function lists all cities with states
    from a db table with username and password
    """
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=_usr, passwd=_pwd, db=_db, charset="utf8"
    )
    cursor = conn.cursor()
    cursor.execute(
        "select cities.name from cities join states \
        on states.id = cities.state_id and states.name = %s",
        (_city,),
    )
    results = cursor.fetchall()
    # print(results)
    print(", ".join([city[0] for city in results]))
    cursor.close()
    conn.close()


if __name__ == "__main__":
    _, _usr, _pwd, _db, _city = tuple(sys.argv)
    get_filter_cities_by_state(_usr, _pwd, _db, _city)
