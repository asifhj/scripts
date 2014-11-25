import MySQLdb
import timing
import time
import sys
import csv
import GeoIP

print "IPs from DB, to LatLon to CSV to JSON."
print "\nConnecting to DB..."

print "\nConnected to DB"

t0 = time.time()
print "\nExecution start time: ", time.asctime()
print "Epoch start time: ", t0
'''
con='';

try:
	# Open database connection
	con = MySQLdb.connect("localhost","root","root","firewall")

	# Prepare a cursor object using cursor() method
	cur = con.cursor()
	
	cur.execute("SELECT VERSION()")

	ver = cur.fetchone()
	
	print "\n\tDatabase version : %s " % ver

	cur.execute("SELECT Distinct(Source_IP), Subtype, Pri, Status_IP  FROM Denied_IPS where Source_IP not like '%10.145.238.222 date=%'")
   	rows = cur.fetchall()
   	counter=0
   	r=[]
	gi = GeoIP.open("/usr/local/share/GeoIP/GeoIPCity.dat",GeoIP.GEOIP_STANDARD)
	
   	with open('some.csv', 'wb') as f:
   		writer = csv.writer(f)
   		r=['Source_IP','Subtype','Pri','Status_IP','country_code','country_code3','country_name','city','region','region_name','postal_code','latitude','longitude','area_code','time_zone','metro_code']
   		writer.writerow(r)
   		r=[]
   		for row in rows:
   				r.append(row[0])
	   			r.append(row[1])
	   			r.append(row[2])
	   			r.append(row[3])
	   			#r.append(row[4])
				gir = gi.record_by_addr(row[0])

				if gir != None:
					r.append(gir['country_code'])
					r.append(gir['country_code3'])
					r.append(gir['country_name'])
					r.append(str(gir['city']))
					r.append(gir['region'])
					r.append(gir['region_name'])
					r.append(gir['postal_code'])
					r.append(gir['latitude'])
					r.append(gir['longitude'])
					r.append(gir['area_code'])
					r.append(gir['time_zone'])
					r.append(gir['metro_code'])
					#print str(gir)
				else:
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
					r.append("NA")
				     #   print str(gir)

	   			writer.writerow(r)
	   			r=[]
	   			counter+=1
	   			#if(counter==3):
	   			#	exit()

except MySQLdb.Error, e:
  
	print "\n\tError %d: %s" % (e.args[0],e.args[1])
	sys.exit(1)
	
finally:    
		
	if con:    
		con.close()
		print "\nDB disconnected."
'''

with open('blacklisted_ips_match_count.csv', 'rb') as fr:
    reader = csv.reader(fr)
    with open('/var/www/globe/population909500.json','w') as fw:
	   fw.write('[')
	   r=''
	   magnitude=0
	   counter=0
	   for row in reader:
	   	if(counter!=0):
	   		if row[12]!="NA":
			   	magnitude=row[4]
			   	latitude=row[12]
				longitude=row[13]
				magnitude=float(float(magnitude)/1000)
				print magnitude
				r+=str(latitude)+","+str(longitude)+","+str(magnitude)+","
		else:
			counter+=1	   
	   r=r[:-1]
	   #print r+"\n"
	   fw.write('\n')
	   fw.write('["1990",[')
	   fw.write(r)
	   fw.write(']],')
	   fw.write('\n')
	   fw.write('["1995",[')
	   fw.write(r)
	   fw.write(']],')
	   fw.write('\n')
	   fw.write('["2000",[')
	   fw.write(r)
	   fw.write(']]')
	   fw.write('\n')
    	   fw.write("]")	

t1 = time.time()
print "\n\tTotal rows: ",counter
print "\nExecution end time: ", time.asctime()
print "Epoch end time: ", t1
total = t1-t0
print "\nTotal taken epoch time: ", total
# disconnect from server
#db.close()