import os
import subprocess

os.system('date')
print "\nWelcome to Memory cleaner and Brightness Controller script .\v"
print "1. To free pagecache:                      \t sync && echo 1 > /proc/sys/vm/drop_caches"
print "2. To free dentries and inodes:            \t sync && echo 2 > /proc/sys/vm/drop_caches"
print "3. To free pagecache, dentries and inodes: \t sync && echo 3 > /proc/sys/vm/drop_caches"
print "4. Increase brigthness					 : \t xbacklight -set '%'"
while(1):
	choice=raw_input("\v\t\aGuess your choice(q to quit): ")
	if(choice.isdigit()):
		if(int(choice)>0 and int(choice)<5): 
			break
	else:
		if(choice=='q' or choice.lower()=='q'):
			print "Exit time: ",os.system('date')
			exit()

if(int(choice)==1):
	print "\v\t\tBefore cleaning\n"
	print "\t\t###############\n"
	os.system("free -mt")
	os.system("sync && echo 1 > /proc/sys/vm/drop_caches")
	print "\v\t\tAfter cleaning\n"
	print "\t\t###############\n"
	os.system("free -mt")
else:
	if(int(choice)==2):
		print "\v\t\tBefore cleaning\n"
		print "\t\t###############\n"
		os.system("free -mt")
		os.system("sync && echo 2 > /proc/sys/vm/drop_caches")
		print "\v\t\tAfter cleaning\n"
		print "\t\t###############\n"
		os.system("free -mt")
	else:
		if(int(choice)==3):
			print "\v\t\tBefore cleaning\n"
			print "\t\t###############\n"
			os.system("free -mt")
			os.system("sync && echo 3 > /proc/sys/vm/drop_caches")
			print "\v\t\tAfter cleaning\n"
			print "\t\t###############\n"
			os.system("free -mt")
		else:
			while (1):
				brightness=raw_input("\v\tEnter brightness value(0-100) or default(4): ")
				if(brightness.isdigit()):
					if(int(brightness)==1):
						os.system("xbacklight -set 30")
						break
					if(int(brightness)>=0 and int(brightness)<=100): 
						os.system("xbacklight -set "+brightness)
						break

print "\vExit time: "
os.system('date')
