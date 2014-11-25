#working for current running jobs
from bs4 import BeautifulSoup
import glob
import os

i=0
os.chdir(".")
for file in glob.glob("Load/currnt*"):
    html_doc=""
    #print file
    with open(file, 'r') as content_file:
        html_doc = content_file.read()
    #print "Loading..."+str(file)
    #print "Processing..."+str(file)+"\n"
    soup = BeautifulSoup(html_doc, "html.parser")
    data_counter=0
    event=""
    table_counter=0
    i = i + 1
    #if i==2:
    #    exit();
    for table in soup.find_all('table'):            
        for row in table.find_all('tr'):
            #for thead in row.find_all('th'):
            #    print(thead.contents)
            for tdata in row.find_all('td'):                        
                temp=tdata.contents[0]
                if data_counter==0:
                    event = event + "SYSDATE=" + str(temp).strip()+":00"
                elif data_counter==1:
                    event = event + " SID=" + str(temp).strip()
                elif data_counter==2:
                    event = event + " JOB=" + str(temp).strip()
                elif data_counter==3:
                    event = event + " SCHEMA_USER=" + str(temp).strip()
                elif data_counter==4:
                    try:
                        event = event + " RUNNING_S=" + str(temp).strip().replace("\n"," ").replace(": ",":")
                    except Exception:
                        event = event + " RUNNING_S=NA"
                elif data_counter==5:
                    event = event + " INTERVAL=" + str(temp).strip()
                elif data_counter==6:
                    event = event + " WHAT=" + str(temp).strip().replace("\n","").replace("  ","")
                data_counter = data_counter + 1
            print event
            event = "";
            data_counter = 0;
            #print "\n"
        table_counter = table_counter + 1
        #print str(table_counter)+"\n\n"

#TO_CHAR(SYSDATE,'   SID     JOB     SCHEMA_USER     RUNNING_S   INTERVAL    WHAT
