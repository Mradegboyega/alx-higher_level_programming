#!/usr/bin/python3
"""
A script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_search = sys.argv[4]

    # Establishing connection
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Base.metadata.bind = engine

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Querying for the first state that matches the argument
        state = session.query(State).filter(State.name == state_name_search).one()
        print(f"{state.id}")
    except NoResultFound:
        print("Not found")

    session.close()

