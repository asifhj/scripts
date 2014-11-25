#Read IPs from text and match with blacklisted IPs


import sys
import csv
import GeoIP
import time
import thread

counter=0
t0 = time.time()
print "\nExecution start time: ", time.asctime()
print "Epoch start time: ", t0	
with open('full_blacklist_database.txt', 'rb') as f:
	found=0	
	for i,black_line in enumerate(f):
		black_line=black_line.split(' ')
		with open('albilad-allowed-ips-count.csv', 'rb') as fr:
			spamreader = csv.reader(fr, delimiter=',')
			for row in spamreader:
    				#print row[39]+"\t"+black_line[0];
				if row[0].strip()==black_line[0].strip():
					found+=1
					print row[0]+"=,"+black_line[0]+","+row[1]+",Blacklisted ip line number: "+str(i)
				#print "\nCounter: "+str(counter)				
				#if counter == 10:
				#	break;
				counter = counter + 1	

print "\n\tTotal: ",found
print "\nExecution end time: ", time.asctime()
t1 = time.time()
print "Epoch end time: ", t1
total = t1-t0
print found
print "\nTotal taken epoch time: ", total
