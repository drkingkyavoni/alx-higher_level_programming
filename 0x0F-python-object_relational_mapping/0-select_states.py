#!/usr/bin/python3

import MySQLdb
import sys

"""
    Module contains get_states function
    Returns: None
"""

def get_states(_usr: str, _pwd: str, _db: str) -> None:
    """
        Function gets state from a db with username and password
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=_usr, passwd=_pwd, db=_db,
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from states order by id asc;")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    _, _usr, _pwd, _db = tuple(sys.argv)
    get_states(_usr, _pwd, _db)
