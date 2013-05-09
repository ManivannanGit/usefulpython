import datetime
import pytz

#from unix time stamp (assuming UTC) to printable time 
createdtime = datetime.datetime.utcfromtimestamp(1368132820)
createdtime = createdtime.replace(tzinfo=pytz.timezone('UTC'))
easterntime = createdtime.astimezone(pytz.timezone('US/Eastern'))
printabletime = easterntime.strftime('%Y-%m-%d %H:%M:%S %Z (%z)') 
