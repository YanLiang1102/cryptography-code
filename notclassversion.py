
p=179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007
import cPickle as pickle
dir="/home/yan/crypresult";
class Stack:
  def __init__(self):
    self.__storage = []
  def isEmpty(self):
    return len(self.__storage) == 0
  def push(self,p):
    self.__storage.append(p)
  def pop(self):
    return self.__storage.pop()


def find_factor_psudeo(n,fac,limit):
	while(fac<limit):
		while(n%fac==0):
			print(fac);
			s.push(fac);
			n=n/fac;
		fac=next_prime(fac)
	if(is_prime_fermat(n)):
		s.push(n);
		return true;
	else:
		return false;

#using fermat to test primability.
def is_prime_fermat(p):
	#a=random_between(2,p);
	R=Integers(p);
	if(R(2)^(p-1)==1):
		return true;
	else:
		return false;

#i use limit as 10^8
base=112889478113369610112883671;
basenumber=R(2)^base
for i in range(0,1001):
	s=Stack();
	basenumber=basenumber*2;
	testnumber=(basenumber).lift();
	if(find_factor_psudeo(testnumber,2,10^8)):
		with open(dir+'/'+str(i)+'.data', 'wb') as output:
    			pickle.dump(s, output, pickle.HIGHEST_PROTOCOL)
		print("I find one answer: "+str(i));

for i in range(0,999):
	s=Stack();
	base=112889478113369610112883671;
	real=base*1000+i;
	testnumber=(R(2)^real).lift();
	if(find_factor_psudeo(testnumber,2,testnumber)):
			with open(dir+'/'+'.data', 'wb') as output:
	    		pickle.dump(s, output, pickle.HIGHEST_PROTOCOL)
			print("I find the answer: "+str(i));


def applyPoly(x,n):
	return (x*x-1)%n;

def generateNextRecord(x,n):
	return applyPoly(applyPoly(x,n),n);

s=Stack();
def find_factor_big(n,x0,limit):
	xnext=generateNextRecord(x0,n);
	diff=xnext-x0;
	candidate=gcd(n,diff);
	#print("candidate: "+str(diff));
	if(candidate!=1 and candidate>=limit):
		print("find big factor: "+str(candidate))
		return [candidate,xnext];
	else :
		return [1,xnext];

def find_factor_psudeo_fast(n,fac,limit):
	while(fac<limit):
		while(n%fac==0):
			print(fac);
			s.push(fac);
			n=n/fac;
		fac=next_prime(fac)
	xstart=100;
	while(n>10^8):
		fac1=find_factor_big(n,xstart,10^8);
		if(fac1[0]!=1):
			n=n/fac1[0];
			s.push(fac1[0])
		xstart=fac1[1]
	if(is_prime_fermat(n)):
		print("I am done and find an answer!");
		return true;
	else:
		print("last divisor and is not a prime "+str(n));
		return false;

with open(dir+'/1.data', 'wb') as output:
    pickle.dump(s, output, pickle.HIGHEST_PROTOCOL)
