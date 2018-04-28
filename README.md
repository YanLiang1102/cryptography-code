# Cryptography Midterm Project Univerysity Of Oklahoma 

```
The two files that are the final code are : headfinal.py and headbash.sh
when you clone the repo on your local need to make chmod +x headbash.sh make it into executable
headfinal.py has the algorithm, and headbash.sh is to create multiple threads to run all of them.

```
## Explanation and how to run the code

need to customize your code in the headbas.sh
"/home/yan/crypfianl/batchfinal" is where you want to store the result
since our power A has to begin with our 27 digits, so the algorithm I am having here and currently running on my machine is:
from base=27digit number
The range of A
from (base*10^8,base*10^8+1*10^6), (base*10^8+1*10^6, base*10^8+2*10^6)........(base*10^8+99*10^6, base*10^8+100*10^6)
so I have 100 processes to run all of them,

for example this is running from (base*10^8,base*10^8+1*10^6) to (base*10^8+base*10^8+9*10^6,base*10^8+10*10^6)
6 means 10^6
8 means 10^8,
1 ,2,3...9 is the beginning of the range.
```
#!/bin/bash
sage headfinal.py 6 8 1 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 6 8 2 "/home/yan/crypfinal/batchfinal/"&

sage headfinal.py 6 8 3 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 6 8 4 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 6 8 5 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 6 8 0 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 6 8 6 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 6 8 7 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 6 8 8 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 6 8 9 "/home/yan/crypfinal/batchfinal/"&
```
since I already explore these spaces basically the space I am explore is:
base=112889478113369610112883671;
1128894781133696101128836710000000000 to 11288947811336961011288367199999999 by doing this 100 times and each time explore 10^6 numbers

say *monique* can run for example
```
#!/bin/bash
sage headfinal.py 9 11 1 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 2 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 3 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 4 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 5 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 0 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 6 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 7 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 8 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 9 "/home/yan/crypfinal/batchfinal/"&
```
*Dong Dong* 
```
sage headfinal.py 9 11 11 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 12 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 13 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 14 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 15 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 10 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 16 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 17 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 18 "/home/yan/crypfinal/batchfinal/"&
sage headfinal.py 9 11 19 "/home/yan/crypfinal/batchfinal/"&
```
so Monique and DongDong can explore
11288947811336961011288367100000000000 (11,'0') to 1128894781133696101128836719999999999 (11, '9')
or you guys can seperate this depends on how much power your computer has.

If you look into the code the basic idea is when factor is small, we explore "finer" in the space, and when the factor get large, 
we use bigger steps to randomly and hope find a factor... so far looks good, and you can turn on and off some of the print statement in headfinal.py and the default is for fac<10^7,we explore everything and from 10^8 to 10^15 we explore some, 
and if you want to explore moredepth deeper in order to find a more smooth stuff but sacrifice the running time,
change moredepth here inside of headfinal.py

```
def main():
    splitrange=sys.argv[1]; #will be 10^6
    intsplitrange=int(splitrange);
    splitfrom=sys.argv[2]; #will be 10^8
    intsplitfrom=int(splitfrom);
    dirbase=sys.argv[4];
    **moredepth=2;** ---change here
    rangestart=sys.argv[3]; #will be like 0,....98
    dir1=dirbase+"total-"+str(splitrange)+"-into-"+str(splitfrom)+"-offset-"+rangestart+"-depth-"+str(moredepth);
    if not os.path.exists(dir1):
        os.makedirs(dir1)
    #10**7 is our limit for the small factor exploring.
    sol=Solution(dir1,10**7,10**intsplitrange,10**intsplitfrom,int(rangestart),False,moredepth);
    sol.execute();
```
## Lattice Attack using BKZ
so the idea here is to explore S'
and build Matrix mm for S' if we can find the solution by using BKZ provided by sage
and then do S-S' and find the smallest one,
my goal is to do 10^80--10^88
so I need to explore all the (10^8-1)*10^8+ target to see if sage can find a solution for those
which we know the first vector returned by sage is the svp solution and out dimension is 101, and last one is 0, 
and previous one is either positive or negative so we look forward to see if the vector length is 10.

