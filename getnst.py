import cPickle as pickle
from sage.all import *
import os
import random
import string
import math

def is_prime_fermat(n):
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
 
def find_factor_psudeo(n,fac,limit,moredepth):
        count=0;
        while(fac<limit):
            while(n%fac==0):
                print(fac);
                n=n/fac;
            fac=next_prime(fac)
        while(fac<limit*10 and count<10**4):
            count=count+1
            fac=next_prime(fac+1000)
            while(n%fac==0):
                print(fac);
                n=n/fac;
         #reset count;
        count=0;
        while(fac<limit*100 and count<10**4):
            count=count+1
            fac=next_prime(fac+10**4)
            while(n%fac==0):
                print(fac);
                n=n/fac;
        count=0;
        #linit=10^7, 3+7=10, so each is 10^9--10^10, need to jump 9*10^9
        while(fac<limit*(10**3) and count<10**4):
            count=count+1
            fac=next_prime(fac+10**5)
            while(n%fac==0):
                print(fac);
                n=n/fac;  
        count=0;
        while(fac<limit*(10**4) and count<10**4):
            count=count+1
            fac=next_prime(fac+10**6)
            while(n%fac==0):
                print(fac);
                n=n/fac;  
        count=0;
        while(fac<limit*(10**5) and count<10**4):
            count=count+1
            fac=next_prime(fac+10**7)
            while(n%fac==0):
                print(fac);
                n=n/fac;
        count=0;
        while(fac<limit*(10**6) and count<10**3):
            count=count+1
            fac=next_prime(fac+10**9)
            while(n%fac==0):
                #s.push(fac)
                n=n/fac;
        count=0;
        #depth=-1
        while(fac<limit*(10**7) and count<10**3):
            count=count+1
            fac=next_prime(fac+10**10)
            while(n%fac==0):
                print(fac);
                n=n/fac;
        count=0;
        #depth=0;
        while(fac<limit*(10**8) and count<10**3):
            count=count+1
            fac=next_prime(fac+10**11)
            while(n%fac==0):
                print(fac);
                n=n/fac;
        #max depth is 10^300,depth at most need to be 150, since the prime at most can be square root
        for depth in range(1,moredepth+1):
            count=0
            while(fac<limit*(10**(8+depth)) and count<10**3):
                count=count+1
            #8+7-1=14
                fac=next_prime(fac+10**(depth+11))
                while(n%fac==0):
                    print(fac)
                    n=n/fac;
        print("remaining from the algorithms:"+str(n));
        if(is_prime_fermat(n)):
            print("yes it is prime");
            return True;
        else:
            print("it is not a prime");
            return False;

            
                

def getFactorizationBest(bestexpo,p):
    R=Integers(p);
    data=(R(2)**bestexpo).lift();
    find_factor_psudeo(data,2,10**7,2)

def fetchBest(rootdir,globalbest):
    solutionDictionary={}
    p=globalbest;
    #looping through all the files under the dir
    for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                 currentfile=os.path.join(subdir,file)
                 with open(currentfile,'rb') as inputdata:
                    data1=pickle.load(inputdata)
                    best=data1["best"];
                    expo=data1["number"]
                    if best<globalbest:
                        globalbest=best;
                        bestexpo=expo;
    solutionDictionary["bit"]=math.log(globalbest*1.0,2);
    solutionDictionary["best"]=globalbest
    solutionDictionary["expo"]=bestexpo;
    print("best bit: "+str(solutionDictionary["bit"]));
    print("best expo: "+str(bestexpo+1));
    print("best remaining is:"+str(globalbest));
    getFactorizationBest(bestexpo+1,p);
  
def main():
    rootdir=sys.argv[1]
    globalbest=179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007;
    fetchBest(rootdir,globalbest);
if __name__ == "__main__":
    main()
