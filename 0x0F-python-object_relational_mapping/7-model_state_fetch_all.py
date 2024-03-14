#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Capture the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a DBSession() instance to establish all conversations with the database
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query for all State objects, ordered by State.id
    states = session.query(State).order_by(State.id.asc()).all()

    # Print each state
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

