T=int(raw_input())
leng=0    
while leng!=T:
	N=raw_input().split(" ")
	leng=len(N)
for n in N:
	i=1
	while i<=int(n):	
		if i%3==0 and i%5==0:
			print "FizzBuzz"
		elif i%3==0:
			print "Fizz"
		elif i%5==0:
			print "Buzz"
		else:
			print i		
		i = i+1
