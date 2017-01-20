#!/usr/bin/python
import sys
import re
from Queue import Queue
from datetime import datetime

q = Queue(maxsize=3)
isFirst=True
currentw=None
previousw=None
prevDate=None

def printReducer():
	wr1=q.get()
	wr2=q.queue[0]
	wr3=q.queue[1]
	spike=0
	avg1=float(wr1["avg_time"])
	avg2=float(wr2["avg_time"])
	avg3=float(wr3["avg_time"])
	if(avg1*2<=avg2 and avg2*2<=avg3):
		spike=1
		print('%s\t%s\t%s' % (wr1["website"],wr1["date"],str(spike)))
	
for line in sys.stdin:
	line=line.strip()
	if(line==''):
		continue
	website,date,avg_time=line.split("\t",3)
	web_record={}
	web_record["website"]=website
	web_record["avg_time"]=avg_time
	web_record["date"]=date
	currentw=website
	date_format = "%Y-%m-%d"
	currDate= datetime.strptime(date, date_format)	
	if isFirst:
		previousw=currentw
		prevDate=currDate
	if currentw==previousw:
		datediff=(currDate-prevDate).days
		if(datediff==1 or datediff==0):
			if(q.qsize()==3):
				printReducer()		
				q.put(web_record)
				previousw=currentw
			else:
				q.put(web_record)
				previousw=currentw
		else:
			if(q.qsize()==3):
				printReducer()
			while not q.qsize()==0:
				q.get()	
			q.put(web_record)
	else:
		if(q.qsize()==3):
			printReducer()
		while not q.qsize()==0:
			q.get()
		previousw=currentw
		q.put(web_record)
	isFirst=False
	prevDate=currDate
if(q.qsize()==3):
	printReducer()
                

