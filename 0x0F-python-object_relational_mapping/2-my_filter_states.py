#!/usr/bin/python3

"""
    Module contains get_states function
    Returns: None
"""


import sys

import MySQLdb


def filter_state(_usr: str, _pwd: str, _db: str, _state: str) -> None:
    """
    Function filters state with specific name
    from a db table with username and password
    """
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=_usr, passwd=_pwd, db=_db, charset="utf8"
    )
    cursor = conn.cursor()
    query = "select * from states where name = '{}' order by id asc".format(
        _state.strip()
    )
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    _, _usr, _pwd, _db, _state = tuple(sys.argv)
    filter_state(_usr, _pwd, _db, _state)
