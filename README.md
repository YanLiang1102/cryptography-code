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
```
for example this is running from (base*10^8,base*10^8+1*10^6) to (base*10^8+base*10^8+9*10^6,base*10^8+10*10^6)
6 means 10^6
8 means 10^8,
1 ,2,3...9 is the beginning of the range.
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

since I already explore these spaces basically the space I am explore is:
base=112889478113369610112883671;
1128894781133696101128836710000000000 to 11288947811336961011288367199999999 by doing this 100 times and each time explore 10^6 numbers

so Monique and DongDong can explore
1128894781133696101128836719999999900000000 (8 '9' and 8 '0') to 1128894781133696101128836719999999999999999 (16 '9')
or you guys can seperate this depends on how much power your computer has.

If you look into the code the basic idea is when factor is small, we explore "finer" in the space, and when the factor get large, 
we use bigger steps to randomly and hope find a factor... so far looks good, and you can turn on and off some of the print statement in headfinal.py and the default is for fac<10**7 we explore everything and from 10**8 to 10**15 we explore some, 
and 





```


