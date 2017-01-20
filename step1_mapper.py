#!/usr/bin/python
import sys
import re
from datetime import datetime
for line in sys.stdin:
	line=line.strip()
	website,stime,etime=line.split("\t",3)
	date=stime[:10]
	starttime=stime[11:]
	endtime=etime[11:]
	#http://stackoverflow.com/questions/3096953/difference-between-two-time-intervals-in-python
	formt='%H:%M:%S'
	time_spent = datetime.strptime(endtime,formt) - datetime.strptime(starttime, formt)
	print('%s\t%s\t%s' %(website,date,time_spent.seconds))
		
