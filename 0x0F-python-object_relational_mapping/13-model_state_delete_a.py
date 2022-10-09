#!/usr/bin/python3
"""deletes a row"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    dbName = argv[3]
    usr = argv[1]
    pass_wd = argv[2]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(usr, pass_wd, dbName), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.ilike('%a%'))
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
