#!/bin/python3

import math
import os
import random
import re
import sys

def solve(a):
    a.sort()
    
    sum_digits = sum(int(digit) for digit in str(a[0]))
  
    if all(x == a[0] for x in a):
        return "NO"  

    for num in a:
        if num % sum_digits == 0:
            return "NO"  
    
    return "YES"  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  
    for t_itr in range(t):
        a_count = int(input().strip())  

        a = list(map(int, input().rstrip().split()))  

        result = solve(a)  

        fptr.write(result + '\n') 

    fptr.close()
