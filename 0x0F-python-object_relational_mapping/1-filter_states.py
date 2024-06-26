#!/usr/bin/python3

"""
    Module contains get_states function
    Returns: None
"""

import sys

import MySQLdb


def filter_states(_usr: str, _pwd: str, _db: str) -> None:
    """
    Function filters state with names that start with 'N'
    from a db table with username and password
    """
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=_usr, passwd=_pwd, db=_db, charset="utf8"
    )
    cursor = conn.cursor()
    cursor.execute("select * from states where name like 'N%' order by id asc")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    _, _usr, _pwd, _db = tuple(sys.argv)
    filter_states(_usr, _pwd, _db)
