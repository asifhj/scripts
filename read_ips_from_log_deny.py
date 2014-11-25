#!/usr/bin/python
import MySQLdb
import time
#import timing
import sys
import thread
import threading
print "IP extraction started!"
print "##allowed####################" 

class read_log(threading.Thread):

    def __init__ (self, m1, m2, m3):
        threading.Thread.__init__(self)
        self.thread_number = m1
        self.startline_number = m2
        self.endline_number = m3

    def run(self):
		# Open database connection
		db = MySQLdb.connect("localhost","root","root","firewall")
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		counter = 0
		line_counter=0
		print "\n"+self.thread_number+" Execution start\tStart line: "+str(self.startline_number)+"\tEnd line: "+str(self.endline_number)
		with open("7","rb",1) as fo:
			for line in fo:
				subtype_start=line.find("subtype=")
				subtype_end=line.find("pri=")
				res1=line[subtype_start+8:subtype_end-1].strip()
				counter+=1
				if counter%50000==0:
					print "\n"+self.thread_number+"\tFile line number: "+str(counter)
				if line_counter>=self.startline_number and line_counter<=self.endline_number and res1=="violation":
					date_start=line.find("date=")
					date_end=line.find("time=")
					time_end=line.find("devname=")

					subtype_start=line.find("subtype=")
					pri_start=subtype_end=line.find("pri=")
					#pri_start=line.find("pri=")
					#pri_end=line.find("status=")
					pri_end=status_start=line.find("status=")
					status_end=line.find("vd=")
					src_start=line.find("src=")
					src_end=line.find("srcname=")
					src_port_start=line.find("src_port=")
					
					dst_start=line.find("dst=")
					dst_end=line.find("dstname=")

					#src_port_end=line.find("")
					dst_port_start=line.find("dst_port=")
					dst_port_end=line.find("service=")
					
					#tran_ip_start=line.find("tran_ip=")
					#tran_ip_end=line.find("tran_port=")
					service_start=line.find("service=")
					service_end=line.find("proto=")
					
					policyid_start=line.find("policyid=")
					policyid_end=line.find("identidx=")
					rule_start=line.find("rule=")
					rule_end=policyid_start
					
					src_int_start=line.find("src_int=")
					src_int_end=dst_int_start=line.find("dst_int")
					dst_int_end=line.find("SN=")
					
					user_start=line.find("user=")
					user_end=line.find("group=")
					#Record details
					log_date=line[0:15]
					date=line[date_start+5:date_end-2]
					time=line[date_end+5:time_end-1]
					src=line[src_start+4:src_end]
					subtype=line[subtype_start+8:subtype_end-1]
					pri=line[pri_start+4:pri_end-1]
					status=line[status_start+7:status_end-1]
					dstname=line[dst_start+4:dst_end-1]
					src_port=line[src_port_start+9:dst_start-1]
					dst_port=line[dst_port_start+9:dst_port_end-1]
					#tran_ip=line[tran_ip_start+8:tran_ip_end-1]
					#tran_port=line[tran_ip_end+10:service_start-1]
					policyid=line[policyid_start+9:policyid_end-1]
					rule=line[rule_start+5:policyid_start-1]
					src_int=line[src_int_start+8:src_int_end-1]
					dst_int=line[dst_int_start+8:dst_int_end-1]
					service=line[service_start+8:service_end-1]
					user=line[user_start+5:user_end-1]
					# Prepare SQL query to INSERT a record into the database.
					sql = "INSERT INTO deny_new(Log_Date, Date, Time, Source_IP, Subtype, Pri, Status_IP, Dst_Name, Src_Port, Dst_Port, PolicyID, Rule, Src_int, Dst_int, Service, User) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (log_date, date, time, src, subtype, pri, status, dstname, src_port, dst_port, policyid, rule, src_int, dst_int, service, user)
					try:
					   # Execute the SQL command
					   cursor.execute(sql)
					   # Commit your changes in the database
					   db.commit()
					except MySQLdb.Error, e:
					   # Rollback in case there is any error
					   print "Error %d: %s" % (e.args[0],e.args[1])
					   db.rollback()		
					
				line_counter+=1
		print "\n"+self.thread_number+" Execution end."
		db.close()
		
#End of function.
threads = []
try:
   thread = read_log ("Thread 0",0, 100000)
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 1",100000, 200000) 
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 2",200000, 300000)  
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 3",300000, 400000) 
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 4",400000, 500000) 
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 5",500000, 600000) 
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 6",600000, 700000) 
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 7",700000, 800000) 
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 8",800000, 900000) 
   thread.start()
   threads.append(thread)
   thread = read_log ("Thread 9",900000, 1000000) 
   thread.start()
   threads.append(thread)
  
   for thread in threads:
	   thread.join()
   
except:
   print "Error: unable to start thread"
