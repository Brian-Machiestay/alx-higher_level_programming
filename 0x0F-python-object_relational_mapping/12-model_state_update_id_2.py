#!/usr/bin/python3
"""updates the states"""

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
    id2 = session.query(State).filter(State.id == 2).one()
    id2.name = "New Mexico"

    session.commit()
    session.close()
