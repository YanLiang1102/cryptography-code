import cPickle as pickle
import sys
import os
from sage.all import *

class Stack():
    def __init__(self):
        self.__storage = []
    def isEmpty(self):
        return len(self.__storage) == 0
    def push(self,p):
        self.__storage.append(p)
    def pop(self):
        return self.__storage.pop()
class Solution():
    p=179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007
    R=Integers(p);
    base=112889478113369610112883671;
    bestSolutionFactor=p;
    def __init__(self,datadir,primebound,offset,expo,range1,bestnameCustom,infoOn):
        '''
        offset is used for each person to start search from a different space.
        we set the boundary prime to be 10^8 to start with.
        '''
        self.__datadir=datadir;
        self.__primebound=primebound;
        self.__offset=offset;
        self.custom=bestnameCustom;
        self.infoOn=infoOn;
        self.range1=range1;
        self.expo=expo;
    def getdir(self):
        return self.__datadir;
    def getOffset(self):
        return self.__offset;
    def random_between(self,j, k) :
        a=int( random()*(k-j+1) ) + j
        return a
    def getPrimeBound(self):
        return self.__primebound;
#     def find_factor_psudeo(self,n,fac,limit,s):
#         while(fac<limit):
#             while(n%fac==0):
#                 if(self.infoOn):
#                     print(fac);
#                 s.push(fac);
#                 n=n/fac;
#             fac=next_prime(fac)
#         if(self.is_prime_fermat(n)):
#             print(n)
#             if(n<self.bestSolutionFactor):
#                 self.bestSolutionFactor=n;
#             s.push(n);
#             return True;
#         else:
#             return False;
    def find_factor_psudeo(self,n,fac,limit,s):
        #while(fac<limit):
        count=0;
        while(fac<limit):
            while(n%fac==0):
#                 if(fac>10**8):
#                     print("try find!!");
#                 if(self.infoOn):
#                     print("fac: "+str(fac));
                s.push(fac);
                n=n/fac;
            if(fac<limit):
                fac=next_prime(fac)
        while(fac<limit*10 and count<10^4):
            count=count+1
            fac=next_prime(fac+1000)
            while(n%fac==0):
                s.push(fac)
                n=n/fac;
        while(fac<limit*10 and count<10^4):
            count=count+1
            fac=next_prime(fac+1000)
            while(n%fac==0):
                s.push(fac)
                n=n/fac;
         #reset count;
        count=0;
        while(fac<limit*100 and count<10**4):
            count=count+1
            fac=next_prime(fac+10**4)
            while(n%fac==0):
                s.push(fac)
                n=n/fac;
         count=0;
        #linit=10^7, 3+7=10, so each is 10^9--10^10, need to jump 9*10^9
         while(fac<limit*(10**3) and count<10**4):
            count=count+1
            fac=next_prime(fac+10**5)
            while(n%fac==0):
                s.push(fac)
                n=n/fac;  
         count=0;
         while(fac<limit*(10**4) and count<10**4):
            count=count+1
            fac=next_prime(fac+10**6)
            while(n%fac==0):
                s.push(fac)
                n=n/fac;  
         count=0;
         while(fac<limit*(10**5) and count<10**4):
            count=count+1
            fac=next_prime(fac+10**7)
            while(n%fac==0):
                s.push(fac)
                n=n/fac;
         count=0;
         while(fac<limit*(10**6) and count<10**3):
            count=count+1
            fac=next_prime(fac+10**8)
            while(n%fac==0):
                s.push(fac)
                n=n/fac;
        if(self.is_prime_fermat(n)):
            print(n)
            if(n<self.bestSolutionFactor):
                self.bestSolutionFactor=n;
            s.push(n);
            return True;
        else:
            return False;
#     def find_factor_advanced(self,n,currentprime):
#         #a little bit twist
#         while(n%primeToTry==0):
#             diff=int(log(n*1.0,2)*0.95);
#             primeToTry=nextPrime(currentprime+diff)
            
                
        
    def is_prime_fermat(self,n):
        '''
        among my test I find like 189 pseudo solutions but only 3 of them are real, and we need to write everything on disk
        so make another test for R(3)
        '''
        #need to recontruct the ring with the special n
        R1=Integers(n)
        if(R1(2)**(n-1)!=1):
            return False;
        else:
            if(R1(3)**(n-1)==1):
                return True;
            else:
                return False;
    def execute(self,looprounds):
        '''
        so we begin A=27 digits,which is (2^10)^9 so it is 2^90,
        and A can goes as big as 2^1024, and each time you multiply 2, we just add 1 to 2^90,
        so we have 2^1024-2^90 times to multiply 2, so have this much space to test on.
        say yan start search add 1 from [0 to 10^12], and monique goes from [10^12+1,2*10^12],
        dong dong is from [2*10^12+1,3*10^12], each person explore like 10^!2 numbers
        so say the offset for monique will be 10^!2, and for dongdong will be 2*10^12,for yan it is 0
        '''
        offset=self.getOffset();
        self.base=self.base+offset;
        basenumber=self.R(2)**self.base;
        boundaryForPrime=self.getPrimeBound();
        datadir=self.getdir();
        for i in range(0,looprounds+1):
            #print("workon: "+str(i));
            s=Stack();
            #after this operation the number is still under the ring R, so still need to lift
            basenumber=basenumber*2;
            testnumber=(basenumber).lift();
            if(self.find_factor_psudeo(testnumber,2,boundaryForPrime,s)):
                #print("I find one answer with offset expo of 10^"+str(self.expo)+"-range"+str(self.range1)+str(i));
                with open(datadir+'/expo-'+str(self.expo)+"-range"+str(self.range1)+"-"+str(i)+'.data', 'wb') as output:
                        pickle.dump(s, output, pickle.HIGHEST_PROTOCOL)         
        #when the whole things is done,save the bestsolution to a file
        with open(datadir+'/exp-'+str(self.expo)+self.custom+"-"+'best.data', 'wb') as output:
                        pickle.dump(self.bestSolutionFactor, output, pickle.HIGHEST_PROTOCOL)
        
def main():
    expo=sys.argv[1]
    range0=sys.argv[2]
    dirbase=sys.argv[3]
    expo1=int(expo)
    range1=int(range0)
    dir1=dirbase+"10-exp-"+str(expo)+"-range-"+range0;
    if not os.path.exists(dir1):
        os.makedirs(dir1)
    sol=Solution(dir1,10**8,10**(expo1)+range1*10**4,expo1,range1,range0+"-"+str(range1+1)+"10000",False);
    sol.execute(10**4);
if __name__ == "__main__":
    main()
        
        
