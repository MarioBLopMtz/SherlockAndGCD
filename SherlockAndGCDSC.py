#!/bin/python3

import math
import os
import random
import re
import sys

def solve(a):
    
    n = len(a)
    for num in a:
        if num == 1:
            return "YES"
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
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
