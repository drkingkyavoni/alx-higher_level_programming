#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine, select, URL


def get_state_filter_a_orm(*args) -> None:
    """
    function lists all states from the database hbtn_0e_6_usa
    """

    dburl = URL.create(
        "mysql+mysqldb",
        username=args[1],
        password=args[2],
        database=args[3],
        host="localhost",
        port=3306,
    )

    engine = create_engine(dburl, pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    with engine.connect() as conn:
        states = conn.execute(
            select(State).where(State.name.like("%a%")).order_by(State.id)
        ).all()

        for state in states:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    get_state_filter_a_orm(*sys.argv)
