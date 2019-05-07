import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine( 'postgresql://postgres:1377159toab@localhost:5432/lecture4')
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print("{} to {}, {} minutes.".format(flight.origin,flight.destination,flight.duration))

if __name__ == "__main__":
    main()
