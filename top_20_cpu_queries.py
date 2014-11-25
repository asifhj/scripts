#working for current running jobs
from bs4 import BeautifulSoup
import glob
import os

i=0
os.chdir(".")
for file in glob.glob("Load/top_20*"):
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
    #if i==2:
    #    exit();
    #print file
    for table in soup.find_all('table'):            
        for row in table.find_all('tr'):
            for tdata in row.find_all('td'):                        
                temp=tdata.contents[0]
                if temp.strip()=="":
                    temp="NA"
                if data_counter==0:
                    event = event + "SYSDATE=" + str(temp).strip()+":00"
                elif data_counter==1:
                    event = event + " SPID=" + str(temp).strip()
                elif data_counter==2:
                    event = event + " SID=" + str(temp).strip()
                elif data_counter==3:                                
                    event = event + " SERIAL=" + str(temp).strip().replace("\n"," ")                    
                elif data_counter==4:
                    event = event + " USERNAME=" + str(temp).strip().replace("\n"," ")                                    
                elif data_counter==5:
                    try:
                        event = event + " MACHINE=" + str(temp).strip().replace("\n","")                    
                    except Exception:
                        event = event + " MACHINE=" + str.encode('utf-8')
                elif data_counter==6:
                    event = event + " LOGON_TIME=" + str(temp).strip()                
                elif data_counter==7:
                    event = event + " RUNNING_S=" + str(temp).strip()                
                elif data_counter==8:
                    event = event + " CPU_USAGE_MINS=" + str(temp).strip()                
                elif data_counter==9:
                    event = event + " SQL_HASH_VALUE=" + str(temp).strip()                
                elif data_counter==10:
                    event = event + " STATUS=" + str(temp).strip().replace("\n","")                    
                elif data_counter==11:
                    try:
                        event = event + " SQL_TEXT=" + str(temp).strip().replace("\n","").replace("  ","")                    
                    except Exception:
                        event = event + " SQL_TEXT=" + str.encode('utf-8')
                elif data_counter==12:
                    event = event + " EVENT=" + str(temp).strip().replace("\n","")                    
                elif data_counter==13:
                    event = event + " SECONDS_IN_WAIT=" + str(temp).strip().replace("\n","")                    
                elif data_counter==14:
                    event = event + " EXECUTIONS=" + str(temp).strip().replace("\n","")                    
                elif data_counter==15:
                    event = event + " USERS_EXECUTING=" + str(temp).strip().replace("\n","")                    
                elif data_counter==16:
                    event = event + " DISK_READS=" + str(temp).strip().replace("\n","")                    
                elif data_counter==17:
                    event = event + " DIRECT_WRITES=" + str(temp).strip().replace("\n","")                    
                elif data_counter==18:
                    event = event + " USER_IO_WAIT_TIME=" + str(temp).strip().replace("\n","") 
                elif data_counter==19:
                    event = event + " APPLICATION_WAIT_TIME=" + str(temp).strip().replace("\n","")                    
                elif data_counter==20:
                    event = event + " CONCURRENCY_WAIT_TIME=" + str(temp).strip().replace("\n","")                    
                elif data_counter==21:
                    event = event + " R=" + str(temp).strip().replace("\n","")                                       

                data_counter = data_counter + 1
            print event
            event = "";
            data_counter = 0;
        table_counter = table_counter + 1
