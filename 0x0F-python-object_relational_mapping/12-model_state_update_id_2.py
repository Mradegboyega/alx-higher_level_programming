#!/usr/bin/python3
"""
A script that changes the name of the State object with id = 2
to "New Mexico" in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    
    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Check if state exists
    if state_to_update:
        # Update state name to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()

