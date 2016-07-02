# fetches the NJT statewide bus feed and dumps it to sqlite
# cron it every minute or 10 seconds or daemon-ize it?

from sqlalchemy import *
from Buses import Bus

Bus.get_data('http://mybusnow.njtransit.com/bustime/map/getBusesForRouteAll.jsp')
print 'Fetching from http://mybusnow.njtransit.com/bustime/map/getBusesForRouteAll.jsp...'

# setup the database connection (per http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html)

db = create_engine('sqlite:///nj_buses_2016.db')

db.echo = False  # Try changing this to True and see what happens

metadata = BoundMetaData(db)

# check if the table exists

if tk:

else:

	# create the table if it doesnt

	position_log = Table('position_log', metadata,
	    Column('position_id', Integer, primary_key=True),
	    Column('lat', Real),
	    Column('lon', Real),
	    Column('headsign', String)
	    Column('destination', String)
	    Column('timestamp', String),
	)
	position_log.create()

# parse the object into the database



# print a summary table of the data collected (number of records, etc)


# write 

# close

