## Question A
Checks a list for duplicate values
## Question B
Due to the fact that the list is being checked for duplicates, every pair of values in the lists have to be compared to see if they match, and thus are duplicates, thus why the algorithm is quadratic in it's worst case.
## Question C
The algorithm is still correct because the values are still being compared as j is simply comparing the value before i, where i has already compared the values so the algorithm will still run correctly.
## Question D
Because j is now running behind i, both i and j no longer have to compare every value together and thus the workload is cut in half as j is simply comparing the value behind i, and the if statement is still valid as i and j will still not equal each other.
## Question E
The time complexity is no longer quadratic as, both i and j are no longer running through every value of the list and comparing them, j is simply running one step behind i, and thus stops one value behind i and checks for duplicates that way as a duplicate will  be found either way as the algorithm still runs through the entire list. 
## Question F
O(n log n)
Source for Time Complexity:https://wiki.python.org/moin/TimeComplexity
## Question G
O(log n)  There is only one n in this algorithm because there one For loop so all of the values have to be checked against N once. 
## Question H
The second algorithm will run faster as it is logaritmic and thus run naturally faster than the first algorithm which is linear and thus with a large input list will run a lot slower. 
## Question I
If they only have 3 elements to check
