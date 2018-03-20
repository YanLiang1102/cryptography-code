# Cryptographic Univerysity Of Oklahoma 
In order to run it, create an instance of the solution:
like this 
```
sol=Solution(dir,10^8,offset)
sol.execute(looprounds)
```
say I want to explore 2^(base+10^6) to 2^(base+2*10^6)
the offset will be 10^6
and looprounds will be 2*10^6-10^6=10^6


Monique need to explore space (10^7---2*10^7),(2*10^7---3*10^7)......(8*10^7---9*10^7)
Dong dong do this:(10^8---2*10^8),(2*10^8---3*10^8)......(8*10^8---9*10^8)

dir should be the directory u want to store your result, preferly for each sol.execute(), you need to give it a different dir,
say (10^7---2*10^7) and (2*10^7---3*10^7) should have different dir to store the result.



///////
in order to batch run do this:
put the batchsage.py
and sagebash.sh in the same dir and make sure you use linux can launch sage from command line by using sage
and then change the parameter in the sagebash.sh and 
chmod +x sagebash.sh
and run it with ./sagebash

---you need tio change the last paramter here to ur own dir
```
Monique
#!/bin/bash
sage batchsage.py 57 1 "/home/yan/crypfinal/batch/"&
sage batchsage.py 57 2 "/home/yan/crypfinal/batch/"&
sage batchsage.py 57 3 "/home/yan/crypfinal/batch/"&
sage batchsage.py 57 4 "/home/yan/crypfinal/batch/"&
sage batchsage.py 57 5 "/home/yan/crypfinal/batch/"&
sage batchsage.py 57 6 "/home/yan/crypfinal/batch/"&
sage batchsage.py 57 7 "/home/yan/crypfinal/batch/"&
sage batchsage.py 57 8 "/home/yan/crypfinal/batch/"&
sage batchsage.py 57 0 "/home/yan/crypfinal/batch/"&
```

```
DongDong:
#!/bin/bash
sage batchsage.py 23 1 "/home/yan/crypfinal/batch/"&
sage batchsage.py 23 2 "/home/yan/crypfinal/batch/"&
sage batchsage.py 23 3 "/home/yan/crypfinal/batch/"&
sage batchsage.py 23 4 "/home/yan/crypfinal/batch/"&
sage batchsage.py 23 5 "/home/yan/crypfinal/batch/"&
sage batchsage.py 23 6 "/home/yan/crypfinal/batch/"&
sage batchsage.py 23 7 "/home/yan/crypfinal/batch/"&
sage batchsage.py 23 8 "/home/yan/crypfinal/batch/"&
sage batchsage.py 23 0 "/home/yan/crypfinal/batch/"&
```

we need to explore base*10^8 then range from offset 0 to 10^6-1
then explore range from offset 10^6...2*10^6
then explore range from offset 2*10^6 to 3*10^6
then explore range from offset 3*10^6 to 4*10^6
...
until explore range from offset 98*10^6 to 99*10^6

in that way we estimately explore 10*6*100=100 milllion records, and they can be run on 100 cores.





and we can at most goes to 
