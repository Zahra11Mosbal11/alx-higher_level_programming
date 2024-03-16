#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    """not be executed when imported"""
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database_name}"
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
