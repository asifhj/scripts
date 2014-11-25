from fractions import gcd
import itertools
import operator

def factor(n):
    """Takes an integer and returns a list of prime factors."""
    i = 2
    factors = []
    while n != 1:
        while n % i == 0:
            n = n // i
            factors.append(i)
        i += 1
    return factors

def display(some_list):
	"""Takes a list of factors and prints to the screen."""
	print(some_list[0])#, end = "")
	if len(some_list) > 1:
		for j in some_list[1:]:
			print(" * " + str(j))#, end = "")
	else:
		print()
N = 0
while(1):
	N = int(raw_input())
	if N>=1 and N<=10:
		break;
i = 1
values = []
while i<=N:
	values.append(raw_input())
	i = i + 1
def lets(A,B):
	c=0		
	aa=factor(A)
	bb=factor(B)
	print aa
	print bb
	alen=len(aa)
	blen=len(bb)
	a=aa[alen-1]
	b=bb[blen-1]
	
	for j in range(A):			
		for k in range(B):			
			if gcd(j,k)==1:
				c=c+1		
	print c				

for v in values:
	vv=v.split(" ")
	a=int(vv[0])
	b=int(vv[1])	
	lets(a,b)

