#!/usr/bin/python3
""" fetch cities by states"""
from sys import argv
from model_state import Base, State
from model_city import City
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
    cities = session.query(State, City)\
                    .filter(State.id == City.state_id)\
                    .order_by(City.id).all()
    for a, u in cities:
        print("{}: ({}) {}".format(a.name, u.id, u.name))
