from datasource import dbconfig, engines
from sqlalchemy import Column, Integer, String, MetaData, Table


# TODO get a connection and do stuff in this main method
# You absolutely must read these docs:
# http://docs.sqlalchemy.org/en/rel_0_9/core/tutorial.html
def main():

    db_engine = engines.get_postgres_engine()

    metadata = MetaData()
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column('fullname', String),
                  )
    metadata.create_all(db_engine)

    print 'line one'
    print 'another line'
    print 'hello world'
    print 'go check the postgres database'




if __name__ == '__main__':
    # execute this block of code if this script is run from command line
    print 'starting main method'
    main()