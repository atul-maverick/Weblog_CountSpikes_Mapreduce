#!/usr/bin/python
import sys

count=0
current_website=None
previous_website=None
isFirst=True

for line in sys.stdin:
	line=line.strip()
	if(line==''):
		continue
	website,date,spike=line.split("\t",3)
	current_website=website
	
	if isFirst:
		previous_website=current_website
	if current_website==previous_website:
		count+=int(spike)
	else:
		print('%s\t%s' % (previous_website,count))
		count=int(spike)
		previous_website=current_website
	isFirst=False

if current_website==previous_website:
	print('%s\t%s' % (current_website,count))
