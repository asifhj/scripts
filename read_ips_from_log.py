#!/usr/bin/python
import MySQLdb
import time
import timing
import sys
print "IP extraction started!"
#Open file to read the events
#Fortigate_Logs/10.145.238.222.20130712-CRC failed in messages/
'''try:
   fo=open("/media/abacus/E-Play/messages-45.2","r",1)
   line=fo.readline()
   subtype_offset_start=line.find("subtype=")
   subtype_offset_end=line.find("pri=")
except IOError as e:
   print "I/O error({0}): {1}".format(e.errno, e.strerror)
   exit()
except ValueError:
   print "Could not convert data to an integer."
except:
   print "Unexpected error:", sys.exc_info()[0]
   raise'''

#print "Name of the file: ", fo.name
#print "Closed or not : ", fo.closed
#print "Opening mode : ", fo.mode
#print "Softspace flag : ", fo.softspace
res=len("allowed")
print "######################" 
#fo.close();
deny=0
access=0
c=0
# Open database connection
db = MySQLdb.connect("localhost","root","root","firewall")

# prepare a cursor object using cursor() method
cursor = db.cursor()
counter = 0
file_seek=0
t0 = time.time()
print "Execution start time: ", time.asctime()
print "Epoch start time: ", t0
with open("/media/abacus/E-Play/messages-45.2","rb",1) as fo:
    for line in fo:
	file_seek+=1
	if file_seek>7200000:
			subtype_start=line.find("subtype=")
			subtype_end=line.find("pri=")
			res1=len(line[subtype_start+8:subtype_end-1].strip())
			counter+=1
			if counter%100000==0:
				print str(counter)+" "+str(deny)+" "+str(file_seek)

			if res!=res1:
				status_start=line.find("status=")
				status_end=line.find("policyid=")
				status=line[status_start+7:status_end-1]
				if status=="deny":
					date_start=line.find("date=")
					date_end=line.find("time=")
					time_end=line.find("devname=")

					src_start=line.find("src=")
					src_end=line.find("srcname=")
					subtype_start=line.find("subtype=")
					subtype_end=line.find("pri=")
					pri_start=line.find("pri=")
					pri_end=line.find("vd=")
					
					dst_start=line.find("dst=")
					dst_end=line.find("dst_port=")

					src_port_start=line.find("src_port=")
					src_port_end=line.find("src_int=")
					dst_port_start=line.find("dst_port=")
					dst_port_end=line.find("dst_int=")
					#Record details
					log_date=line[0:15]
					date=line[date_start+5:date_end-2]
					time=line[date_end+5:time_end-1]
					src=line[src_start+4:src_port_start]
					subtype=line[subtype_start+8:subtype_end-1]
					pri=line[pri_start+4:pri_end-1]
					
					dstname=line[dst_start+4:dst_end-1]
					src_port=line[src_port_start+9:src_port_end-1]
					
					service_start=line.find("dst_country=")
					dst_port=line[dst_port_start+9:dst_port_end-1]
					others=line[service_start:]
					#print '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (log_date, date, time, src, subtype, pri, status, dstname, src_port, dst_port, others)
					#print "\n\n"+dst_port
					
					#print line
					#print "\n\n##### "
					# Prepare SQL query to INSERT a record into the database.
					sql = "INSERT INTO Denied_IPS_B(Log_Date, Date, Time, Source_IP, Subtype, Pri, Status_IP, Dst_Name, Src_Port, Dst_Port, Others) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (log_date, date, time, src, subtype, pri, status, dstname, src_port, dst_port, others)
					try:
					   # Execute the SQL command
					   cursor.execute(sql)
					   # Commit your changes in the database
					   db.commit()
					except MySQLdb.Error, e:
					   # Rollback in case there is any error
					   print "Error %d: %s" % (e.args[0],e.args[1])
					   db.rollback()
					deny=deny+1						
			else:
				access=access+1
	else:
		if file_seek%100000==0:
				print str(file_seek)
print "Denied: ",deny
print "Accessed: ",access
t1 = time.time()
print "Execution end time: ", str(time.asctime())
print "Epoch end time: ", t1
total = t1-t0
print "Total taken epoch time: ", total
# disconnect from server
db.close()

#Close a file
fo.close()
