#!/usr/bin/python3
"""
Lists all State objects that contains the letter a from db hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Verification of all required arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Command line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connection to SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database),
        pool_pre_ping=True
    )

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the first object State by id
    states = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id.asc()).all()

    # Print result
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
