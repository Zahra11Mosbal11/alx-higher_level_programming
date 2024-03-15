#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """not be executed when imported"""
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database_name}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()
