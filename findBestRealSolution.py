import cPickle as pickle
from sage.all import *
import os
import random
import string

class Stack():
    def __init__(self):
        self.__storage = []
    def isEmpty(self):
        return len(self.__storage) == 0
    def push(self,p):
        self.__storage.append(p)
    def pop(self):
        return self.__storage.pop()



def findTheRealSmallestPrime(rootdir,globalbest):
    solutionDictionary={}
    solutioncount=0;
    bestfile="";
    globalbest="";
    #looping through all the files under the dir
    for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                 currentfile=os.path.join(subdir,file)
                 with open(currentfile,'rb') as inputdata:
                    data1=pickle.load(inputdata)
                    first=data1.pop();
                    #print(first)
                    #if first.is_prime():
                        #print("yes")
                    if first<globalbest:
                        globalbest=first
                        bestfile=currentfile
                    solutioncount=solutioncount+1;
                    solutionDictionary[str(first)]=file;                          
    #store the solution dictionary and the best solution find on disk.
    solutionDictionary["solutioncount"]=solutioncount;
    solutionDictionary["globalbest"]=globalbest;
    solutionDictionary["bestfile"]=bestfile;
    randomstring=''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
    with open(rootdir+"/best-"+randomstring+".best", 'wb') as output:
                        pickle.dump(solutionDictionary, output, pickle.HIGHEST_PROTOCOL)
                        print(rootdir+"/best-"+randomstring+".best")

def main():
    rootdir=sys.argv[1]
    globalbest=179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007;
    findTheRealSmallestPrime(rootdir,globalbest)
if __name__ == "__main__":
    main()
