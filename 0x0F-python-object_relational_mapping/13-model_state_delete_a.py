#!/usr/bin/python3
"""
    deletes States that contains 'a' letter.
"""
import sys
from sqlalchemy import create_engine, collate
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like(r"%a%")).delete()
    session.commit()
    session.close()
    engine.dispose()
