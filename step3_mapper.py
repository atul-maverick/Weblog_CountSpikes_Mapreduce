#!/usr/bin/python
import sys
import re
from Queue import Queue

q = Queue(maxsize=3)

for line in sys.stdin:
	line=line.strip()
	if(line==''):
		continue
	website,date,spike=line.split("\t",3)
	
	print('%s\t%s\t%s' % (website,date,spike))
	

	
                

