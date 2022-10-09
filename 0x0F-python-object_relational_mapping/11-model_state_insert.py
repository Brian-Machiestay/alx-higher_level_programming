#!/usr/bin/python3
"""adds the State object “Louisiana” to the database"""
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
    lousi = State(name="Louisiana")
    session.add(lousi)
    get_lousi = session.query(State).filter(State.name == "Louisiana").first()
    print("{}".format(get_lousi.id))

    session.commit()
    session.close()
