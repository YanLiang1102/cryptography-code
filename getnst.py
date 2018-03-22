import cPickle as pickle
from sage.all import *
import os
import random
import string
import math
def fetchBest(rootdir,globalbest):
    solutionDictionary={}
    bestbit=1024;
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
    print("best expo: "+str(bestexpo));
    print("best remaining is:"+str(globalbest));
    
def main():
    rootdir=sys.argv[1]
    globalbest=179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007;
    fetchBest(rootdir,globalbest);
if __name__ == "__main__":
    main()
