import sys
import os
import pickle
from sage.all import *
import random
import math
import pickle

# def getMlist(mlist):
#     #with open('/Users/yanliang/cryptography/madata.data', 'a') as the_file:
#     p=2;
#     count=0;
#     while(count<100):
#         #data=math.floor((p)**(1/3)*(10**100));
#         data=math.floor(((ZZ(p).n(prec=1000).nth_root(3))*(10**100))
#         #the_file.write(str(data)+'\n');
#         mlist.append(data);
#         count=count+1;
#         p=next_prime(p)
    #return mlist;
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
    while(count<100):
        #data=math.floor((p)**(1/3)*(10**100));
        data=math.floor(((ZZ(p).n(prec=1000).nth_root(3))*(10**100)))
        #the_file.write(str(data)+'\n');
        mlist[count]=data;
        count=count+1;
        p=next_prime(p)
    ar=[0,
 1,
 0,
 0,
 1,
 0,
 0,
 0,
 0,
 1,
 0,
 0,
 0,
 0,
 0,
 1,
 0,
 0,
 0,
 0,
 0,
 0,
 1,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 1,
 1,
 0,
 0,
 0,
 0,
 0,
 1,
 0,
 1,
 0,
 0,
 1,
 1,
 0,
 0,
 0,
 0,
 1,
 1,
 0,
 1,
 0,
 1,
 0,
 1,
 1,
 1,
 1,
 1,
 0,
 1,
 0,
 1,
 1,
 1,
 0,
 1,
 0,
 0,
 0,
 0,
 1,
 0,
 0,
 1,
 1,
 1,
 0,
 0,
 1,
 1,
 0,
 1,
 1,
 1,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 1];
    fixed=[2,
 4,
 7,
 13,
 14,
 16,
 17,
 19,
 20,
 23,
 24,
 25,
 30,
 31,
 32,
 34,
 37,
 38,
 39,
 40,
 41,
 47,
 49,
 50,
 54,
 56,
 57,
 59,
 60,
 64];
 #seperate into 2^5=0,1,2,...31 thread to do so each thread will handle 2^25
    sumInMemory=[]
    start=(2**25)*intindex
    for i in range(start,(2**25)+start):
        t=intToB(i)
        data=0;
        for i in range(len(t)-1,-1,-1):
            data=data+((int)(t[i]))*mlist[fixed[i]];
        sumInMemory.append(data);
    with open('/home/yan/crypdata/fixed'+str(intindex)+".data", 'wb') as handle:
        pickle.dump(sumInMemory, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
