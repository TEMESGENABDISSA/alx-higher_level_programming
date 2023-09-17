#!/usr/bin/python3
"""let's  prints State object with the name passed
    as argument from the database.
    (SQL injection free)
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    name = argv[4]
    Sn = State.name
    states = session.query(State) \
                    .filter(Sn == name).first()

    if states is None:
        print("Not found")
    else:
        print('{}'.format(states.id))
