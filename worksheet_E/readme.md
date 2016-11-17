

##Question A
```
s2 = 0
s3 = s0

while s3 != 0:
    s2 += s1
    s3 -= 1
```
##Question B
```
As the loop is only re-executed while s3 is not equal to  zero, and each time the loop is run s1 is added to s2, and as s2 is set to zero at the start of the program, this means that s1 times s0 will be the value of 2, I.E. if the loop runs once, s1, which has the value of 1 will be added to s2 making it have the value of 1, thus having the effect of multiplying S1 and S2.
```
##Question C
```
S0 = 10
S1 = 1

    while S0 !=0:
        S2 = 0
        S3 = S0
        
        while S3 !=0:
        S2 += S1
        S3 -= 1
        
        S1 = S2
        S0 -= 1
```
##Question D
The outer loop of the of the code is tied to the the fact that S0 is not equal to zero and as it is set to be 10, and id decreased by one at the end of the code it will run until it hits zero, a total of ten times.

The inner loop then is tied to S3 and as S3 is set to equal S0 and thus also runs a total of 10 times.

And thus by running this loop it is timesing the value of s1 by the value of S3, then after that it is set to equal S2 so that at the end of the first run s1 equals 1 and thus is equal to the factorial of the value of S0 as the code goes on. 


