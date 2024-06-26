#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine, select


def get_all_states_orm(*args) -> None:
    """
    function lists all states from the database hbtn_0e_6_usa
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(args[1], args[2], args[3]),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(bind=engine)

    with engine.connect() as conn:
        states = conn.execute(select(State).order_by(State.id)).fetchall()

        for state in states:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    get_all_states_orm(*sys.argv)
