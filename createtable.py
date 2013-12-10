from datasource import dbconfig, engines
from sqlalchemy import Column, Integer, String, MetaData, Table
import csv

def main():

    db_engine = engines.get_postgres_engine()

    metadata = MetaData()
    people = Table('people', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('first_name', String),
                  Column('last_name', String),
                  Column('age', Integer)
                  )
    metadata.create_all(db_engine)
    
    data = csv.DictReader(open("test.csv"))

    for row in data:

    db_engine.execute(people.insert(), [data])

if __name__ == '__main__':
    # execute this block of code if this script is run from command line
    print 'starting main method'
    main()