#!/usr/bin/python3
#A cumulative sum is a collection of partial sums from a given set of lists or data frames.
# Please do not change the below function name and parameters
def csum(n):
    k = []
    for i in range(len(n)):
        s = 0
        for j in range(i + 1):
            s = s + n[j]
            pass
        k.append(s)
        pass
    print(k)
    pass
# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
     
csum(lst)
