#!/usr/bin/python3
"""
This script prints the first State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    
  
    first_state = session.query(State).order_by(State.id).first()
    
    if first_state:
        print("{0}: {1}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
