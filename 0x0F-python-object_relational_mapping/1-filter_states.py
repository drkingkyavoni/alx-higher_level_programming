#!/usr/bin/python3

import MySQLdb
import sys

"""
    Module contains get_states function
    Returns: None
"""

def filter_states(_usr: str, _pwd: str, _db: str) -> None:
    """
        Function filters state with names that start with 'N'
        from a db with username and password
    """
    cursor = ""

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=_usr, passwd=_pwd, db=_db)
        cursor = conn.cursor()
        query = "select * from states where name like 'N%';"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as err:
        print(f"Connection failed on {_db}: {err}")
    finally:
        if cursor:
            cursor.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py username password database")
        sys.exit(1)

    _, _usr, _pwd, _db = tuple(sys.argv)
    filter_states(_usr, _pwd, _db)