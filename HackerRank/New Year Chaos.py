#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    n: int = len(q)
    i: int = n - 1
    
    cnt: int = 0
    flag: bool = True
    while flag and i > 0:
        if q[i] != i + 1:
            if i + 1 == q[i-1]:
                cnt += 1
                q[i], q[i-1] = q[i-1], q[i]

            elif i-1 >= 0 and i + 1 == q[i-2]:
                cnt += 2
                q[i-1], q[i-2] = q[i-2], q[i-1]
                q[i], q[i-1] = q[i-1], q[i]

            else:
                # print("i: ", i)
                flag = False
        i -= 1
    
    if flag:
        print(cnt)
    else:
        print("Too chaotic")
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
