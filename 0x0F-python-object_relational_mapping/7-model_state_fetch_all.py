#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    """
    function lists all states from the database hbtn_0e_6_usa
    """

    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(bind=engine)

    with engine.connect() as conn:
        states = conn.execute(select(State).order_by(State.id)).fetchall()

        for state in states:
            print(f"{state.id}: {state.name}")
