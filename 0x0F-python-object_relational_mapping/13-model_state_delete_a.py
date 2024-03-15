#!/usr/bin/python3
"""
A script that deletes all State objects with names containing the letter 'a'
from the database hbtn_0e_6_usa.
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

    # Query for states containing 'a' in their names
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete these states
    for state in states_to_delete:
        session.delete(state)
    
    # Commit the changes
    session.commit()

    # Close the session
    session.close()

