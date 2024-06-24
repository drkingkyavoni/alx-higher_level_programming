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
    cursor = ""

    try:
        # print(f'{_usr}@{_db}.localhost:{_pwd}')
        conn = MySQLdb.connect(host="localhost", port=3306, user=_usr, passwd=_pwd, db=_db)
        cursor = conn.cursor()
        query = "select * from states order by id asc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except MySQLdb.Error as err:
        print(f"Connection to {_db} failed: {err}")
    finally:
        if cursor:
            cursor.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py username password database")
        sys.exit(1)

    _, _usr, _pwd, _db = tuple(sys.argv)
    get_states(_usr, _pwd, _db)