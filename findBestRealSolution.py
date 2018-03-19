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
solutioncount=0;
globalbest=179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007;
solutionDictionary={}
def findTheRealSmallestPrime(rootdir):
    #looping through all the files under the dir
    for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                 currentfile=os.path.join(subdir,file)
                 with open(currentfile  , 'rb') as inputdata:
                    data=pickle.load(inputdata)
                    first=data.pop()
                    if first.is_prime():
                        globalbest=Math.min(globalbest,first);
                        solutioncount=solutioncount+1;
                        solutionDictionary[str(first)]=file;                          
    #store the solution dictionary and the best solution find on disk.
    solutionDictionary["solutioncount"]=solutioncount;
    solutionDictionary["globalbest"]=globalbest;
    randomstring= random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
    with open(rootdir+"/best-"+randomstring+".best", 'wb') as output:
                        pickle.dump(solutionDictionary, output, pickle.HIGHEST_PROTOCOL)

def main():
    rootdir=sys.argv[1]
    findTheRealSmallestPrime(rootdir)
if __name__ == "__main__":
    main()
