#https://en.wikipedia.org/wiki/Swatch_Internet_Time
#https://stackoverflow.com/questions/51721018/swatch-internet-time-in-python
#https://dateutil.readthedocs.io/en/stable/tz.html
#https://www.swatch.com/en_us/internet-time/
#http://www.swatchclock.com/


##TODO
##Refactoring

##DONE
##Steps to follow
##Get UTC time
##Convert UTC time to Switzerland Time
##Convert Switzerland Time to seconds
##Convert seconds to Beats
##Print out

from datetime import datetime, date, time, timezone
from dateutil import tz

##Defining source and target timezones
UTC_zone = tz.gettz('UTC')
Zurich_zone = tz.gettz('Europe/Zurich')

##Getting time from the source and target timezones
time=datetime.utcnow()
UTC_time = time.replace(tzinfo=UTC_zone)
Zurich_time = UTC_time.astimezone(Zurich_zone)

##Printing time for diagnostic purpose: uncomment if needed
##print(UTC_time)
##print(Zurich_time)

##Converting target time to hours, minutes and seconds 
hours, minutes, seconds = Zurich_time.timetuple()[3:6]

##Converting time into seconds, adjusting to Biel time, then converting to beats
time_in_seconds = ((hours*3600) + (minutes*60) + (seconds)) - 3600
beats = time_in_seconds/86.4

##Clamping beats value to min and max values of 0 and 1000
if beats > 1000:
    beats -= 1000
elif beats < 0:
    beats += 1000

print("The current Internet Time is @" +  str(beats))
