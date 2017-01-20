#!/usr/bin/python
import sys

count=0
current_combo=None
previous_combo=None
avg_time=0
isFirst=True

for line in sys.stdin:
	line=line.strip()
	if(line==''):
		continue
	website,date,time_spent=line.split("\t",3)
	current_combo=website+"\t"+date
	
	if isFirst:
		previous_combo=current_combo
	if current_combo==previous_combo:
		count+=1
		avg_time+=float(time_spent)
	else:
		avg_time=avg_time/count
		print('%s\t%s' % (previous_combo,avg_time))
		count=1
		avg_time=float(time_spent)
		previous_combo=current_combo
	isFirst=False

if current_combo==previous_combo:
	avg_time=avg_time/count
	print('%s\t%s' % (current_combo,avg_time))
