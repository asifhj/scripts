#working for current running jobs
from bs4 import BeautifulSoup
import glob
import os

i=0
os.chdir(".")
for file in glob.glob("Load/pending*"):
    html_doc=""
    
    with open(file, 'r') as content_file:
        html_doc = content_file.read()
    #print "Loading..."+str(file)
    #print "Processing..."+str(file)+"\n"
    soup = BeautifulSoup(html_doc, "html.parser")
    data_counter=0
    event=""
    table_counter=0
    i = i + 1
    for table in soup.find_all('table'):            
        for row in table.find_all('tr'):            
            for tdata in row.find_all('td'):                        
                temp=tdata.contents[0]
                if temp.strip()=="":
                    temp="NA"
                if data_counter==0:
                    event = event + "SYSDATE=" + str(temp).strip()+":00"
                elif data_counter==1:
                    event = event + " JOB=" + str(temp).strip()
                elif data_counter==2:
                    event = event + " SCHEMA_USER=" + str(temp).strip()
                elif data_counter==3:            
                    event = event + " NEXT_DATE=" + str(temp).replace("\n"," ")                    
                elif data_counter==4:                    
                    event = event + " INTERVAL=" + str(temp).strip().replace("\n"," ")                    
                elif data_counter==5:
                    event = event + " WHAT=" + str(temp).strip().replace("\n"," ").replace("                   "," ").replace("  "," ")                                                                    
                data_counter = data_counter + 1
            print event
            event = "";
            data_counter = 0;
        table_counter = table_counter + 1
print i
#
#TO_CHAR(SYSDATE,'   SID     JOB     SCHEMA_USER     RUNNING_S   INTERVAL    WHAT
