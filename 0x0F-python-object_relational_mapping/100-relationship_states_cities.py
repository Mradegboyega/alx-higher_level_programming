#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco"
   in the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Create a new State
    california = State(name="California")

    # Create a new City
    san_francisco = City(name="San Francisco")

    # Add San Francisco to California
    california.cities.append(san_francisco)

    # Add California and San Francisco to the session
    session.add(california)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()

