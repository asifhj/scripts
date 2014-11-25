while(1):
	n = int(raw_input())
    	if n>3 and n<100:
    		break

table = [ raw_input().split(",") for j in range(n) ]
m = []
for t in table:
	m.append([int(x) for x in t])
op = raw_input()

for o in op:
	if o=="A":		
		m = zip(*m)[::-1]
	elif o=="C":
		m = zip(*m[::-1])	
	elif o=="T":
		m = zip(*m)	
	elif o=="/":
		m = zip(*zip(*zip(*m))[::-1])[::-1]
	elif o=="\\":				
		m = zip(*zip(*zip(*m[::-1]))[::-1])
for i in m:
	print(",".join(str(e) for e in i ))

