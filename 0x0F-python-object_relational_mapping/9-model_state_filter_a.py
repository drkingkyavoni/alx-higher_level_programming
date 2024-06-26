#!/usr/bin/python3
"""
Function lists all State objects from the database hbtn_0e_6_usa
Return: None
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    """
    print all states from the database hbtn_0e_6_usa
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
        states = conn.execute(
            select(State).where(State.name.like("%a%")).order_by(State.id)
        ).all()

        for state in states:
            print(f"{state.id}: {state.name}")
