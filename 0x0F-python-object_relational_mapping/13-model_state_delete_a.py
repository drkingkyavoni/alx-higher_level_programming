#!/usr/bin/python3
"""
Function to delete a State object from the database hbtn_0e_6_usa
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.engine.url import URL

if __name__ == "__main__":
    """
    delete a state from the database hbtn_0e_6_usa
    """

    if len(sys.argv) != 4:
        sys.exit(1)

    dburl = URL.create(
        drivername="mysql+mysqldb",
        username=sys.argv[1],
        password=sys.argv[2],
        host="localhost",
        port=3306,
        database=sys.argv[3],
    )

    engine = create_engine(dburl, encoding="latin1")

    Base.metadata.create_all(bind=engine)

    with engine.connect() as conn:
        state = conn.execute(delete(State).where(State.name.like("%a%")))
