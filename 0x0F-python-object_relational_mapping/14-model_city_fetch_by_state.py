#!/usr/bin/python3
"""
 let's   Prints all of the  City objects from the database.
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    cities = session.query(State, City) \
                    .filter(State.id == City.state_id)

    for c in cities:
        print("{}: ({:d}) {}".format(c.State.name, c.City.id, c.City.name))

    session.close()
