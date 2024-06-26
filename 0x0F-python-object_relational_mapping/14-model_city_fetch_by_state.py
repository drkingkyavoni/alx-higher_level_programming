#!/usr/bin/python3
"""
lists Cities in a State from the database hbtn_0e_6_usa
"""

import sys

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.engine.url import URL

if __name__ == "__main__":
    """
    print cities in a state from the database hbtn_0e_6_usa
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
        results = conn.execute(
            select(State.name, City.id, City.name)
            .join_from(State, City, City.state_id == State.id)
            .order_by(City.id)
        ).fetchall()

        for row in results:
            print(f"{row[0]}: ({row[1]}) {row[2]}")
