import sys
import os
import pickle
from sage.all import *
import random
import math
import pickle

def constructMatrix(target,mlist):
    #construct a matrix with dimension 101*101
    dim=101
    dim1=100;
    mm=Matrix.identity(dim);
    #then update the matrix;
    mm=2*mm;
    for i in range(0,dim1):
        mm[i,dim1]=mlist[i]
        mm[dim1,i]=1
    mm[dim1,dim1]=target;
    return mm;


def intToB(x):
    return ("{0:b}".format(x))   
        
def main():
    index=sys.argv[1]; #will be 10^6
    #print(index);
    intindex=(int)(index);
    #new code
    mlist=[0]*100;
    p=2;
    count=0;
    target=2*112889478*(10**94);
    while(count<100):
        #data=math.floor((p)**(1/3)*(10**100));
        data=math.floor(((ZZ(p).n(prec=1000).nth_root(3))*(10**100)))
        #the_file.write(str(data)+'\n');
        mlist[count]=data;
        count=count+1;
        p=next_prime(p)
 #seperate into 2^5=0,1,2,...31 thread to do so each thread will handle 2^25
    rst=[]
    for diff in range(0,10**6):
        #take one every 1000 steps the idea here is to explore the 10^80--10^90.
        mm=constructMatrix((target+(diff+intindex*10**6)*1000)*(10**80),mlist);
        tt=(float)(mm.LLL()[0].norm());
        #print(tt);
        if(diff%(10**4)==0):
            print("working on index: "+str(diff));
        if(tt==10):
            print("find: "+str(diff));
            rst.append(diff);
    with open('/home/yan/crypdata/fixed/bkz/bkz.data', 'wb') as handle:
        pickle.dump(rst, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    main()

