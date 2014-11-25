import os
path = "/media/abacus/E-Play/Hans Zimmer - Man Of Steel (Original Motion Picture Soundtrack) [Deluxe Edition] 2013 OST 320kbps CBR MP3 [VX] [P2PDL]"
for (path, dirs, files) in os.walk(path):
    #print dirs
    #print files
    for f in files:
    	print len(f)
		if(f[l-4:l]=="pdf"):
	        print f
print l 