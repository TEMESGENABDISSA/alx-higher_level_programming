#!/usr/bin/python3
"""Return or print  the 1rst State object"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=False)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    states = session.query(State).order_by(State.id).first()

    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))

    session.close()
