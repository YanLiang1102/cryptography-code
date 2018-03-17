import cPickle as pickle
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
    def __init__(self,datadir,primebound,offset):
        '''
        offset is used for each person to start search from a different space.
        we set the boundary prime to be 10^8 to start with.
        '''
        self.__datadir=datadir;
        self.__primebound=primebound;
        self.__offset=offset;
    def getdir(self):
        return self.__datadir;
    def getOffset(self):
        return self.__offset;
    def getPrimeBound(self):
        return self.__primebound;
    def find_factor_psudeo(self,n,fac,limit,s):
        while(fac<limit):
            while(n%fac==0):
                print(fac);
                s.push(fac);
                n=n/fac;
            fac=next_prime(fac)
        if(self.is_prime_fermat(n)):
            if(n<self.bestSolutionFactor):
                self.bestSolutionFactor=n;
            s.push(n);
            return True;
        else:
            return False;
    def is_prime_fermat(self,n):
        #need to recontruct the ring with the special n
        R1=Integers(n)
        if(R1(2)^(n-1)==1):
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
        basenumber=self.R(2)^self.base;
        boundaryForPrime=self.getPrimeBound();
        datadir=self.getdir();
        for i in range(0,looprounds+1):
            s=Stack();
            #after this operation the number is still under the ring R, so still need to lift
            basenumber=basenumber*2;
            testnumber=(basenumber).lift();
            if(self.find_factor_psudeo(testnumber,2,boundaryForPrime,s)):
                print("I find one answer: "+str(offset)+"-"+str(i));
                with open(datadir+'/'+str(offset)+"-"+str(i)+'.data', 'wb') as output:
                        pickle.dump(s, output, pickle.HIGHEST_PROTOCOL)         
        #when the whole things is done,save the bestsolution to a file
        with open(datadir+'/'+str(offset)+"-"+'best.data', 'wb') as output:
                        pickle.dump(self.bestSolutionFactor, output, pickle.HIGHEST_PROTOCOL)
        
           
        
