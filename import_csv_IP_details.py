#Import from GeoLiteCity CSV to database
import csv
import MySQLdb
import time
import sys
counter = 0
column_values = []
row_no = 0
'''
#For all columns
# Open database connection
db = MySQLdb.connect("localhost","root","root","alert_log")

# prepare a cursor object using cursor() method
cursor = db.cursor()

t0 = time.time()
print "Execution start time: ", time.asctime()
print "Epoch start time: ", t0

try:
	with open('Alert_Details_ETMP-FE-WT-EC_20130927_141212.csv','rb',1) as csv_input:
		reader=csv.reader(csv_input)
		for row in reader:
			if(row_no>1):
	    			for col in row:
					column_values.append(col)
				i=iter(column_values)
				sql = "INSERT INTO alert(alertType,alertid,product,releasee,fileHash,dvchost,sname,dvc,locations,malware_type,sev,occurred,mwurl,link,src1,action,objurl,sid,stype,profile,malwarenote,application,original_name,header,anomaly,osinfo,cnchost,channel,cncport,os,app,src,shost,spt,smac,dst,dmac,dpt) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s')" % (''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()),''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()),''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()),''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()),''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()),''+str(i.next()), ''+str(i.next()), ''+str(i.next()), ''+str(i.next()))
				try:
				   # Execute the SQL command
				   cursor.execute(sql)
				   
				   
				except MySQLdb.Error, e:
				   # Rollback in case there is any error
				   print "Error %d: %s" % (e.args[0],e.args[1])
				   print "\n\tRow No: %s",row_no
				   #db.rollback()
				row_no+=1				
				column_values=[]
			else:
				row_no=row_no+1
except IOError as e:
   print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
   print "Could not convert data to an integer."
except:
   print "Unexpected error:", sys.exc_info()[0]
   raise
   
t1 = time.time()
print "Execution end time: ", time.asctime()
print "Epoch end time: ", t1
total = t1-t0
print "Total taken epoch time: ", total
print "Rows inserted: ", row_no
# Commit your changes in the database
db.commit()
# disconnect from server
db.close()'''


#For single colum extraction.
# Open database connection
db = MySQLdb.connect("localhost","root","root","alert_log")

# prepare a cursor object using cursor() method
cursor = db.cursor()

t0 = time.time()
print "Execution start time: ", time.asctime()
print "Epoch start time: ", t0

try:
	with open('Alert_Details_ETMP-FE-WT-EC_20130927_141212.csv','rb',1) as csv_input:
		reader=csv.reader(csv_input)
		for row in reader:
			if(row_no>1):
				sql = "INSERT INTO alert_ip(src) VALUES ('%s')" % (''+str(row[14]))
				try:
				   # Execute the SQL command
				   cursor.execute(sql)
				   
				   
				except MySQLdb.Error, e:
				   # Rollback in case there is any error
				   print "Error %d: %s" % (e.args[0],e.args[1])
				   print "\n\tRow No: %s",row_no
				   #db.rollback()
				row_no+=1				
				column_values=[]
			else:
				row_no=row_no+1
except IOError as e:
   print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
   print "Could not convert data to an integer."
except:
   print "Unexpected error:", sys.exc_info()[0]
   raise
   
t1 = time.time()
print "Execution end time: ", time.asctime()
print "Epoch end time: ", t1
total = t1-t0
print "Total taken epoch time: ", total
print "Rows inserted: ", row_no
# Commit your changes in the database
db.commit()
# disconnect from server
db.close()
