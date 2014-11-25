#!/usr/bin/python
import numpy as np

while(1):
	n = int(raw_input())
    	if n>1:
    		break

table = [ raw_input().split(",") for j in range(n) ]
table1 = []
for t in table:
	table1.append([int(x) for x in t])
op = raw_input()

mat = table1


a=op.count("A")
c=op.count("C")
tt=op.count("T")
#print o+"	Start"
m = mat
for o in op:
	if o=="A":		
		m = zip(*m)[::-1]
	elif o=="C":
		m = zip(*m[::-1])	
	elif o=="T":
		m = zip(*m)	
	elif o=="/":
		m = zip(*m)
		m = zip(*m)[::-1]
		m = zip(*m)[::-1]
	elif o=="\\":
		m = zip(*m[::-1])
		m = zip(*m[::-1])
		m = zip(*m)
i = 0 
for t in m:
	row = ""
	for e1 in t:
		if i<5:
			row = row + str(e1)+","		
		else:
			row = row + str(e1)		
		i = i + 1	
	i=0
	print row[0:len(row)-1]		

