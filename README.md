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

