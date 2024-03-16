#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """not be executed when imported"""
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database_name}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
