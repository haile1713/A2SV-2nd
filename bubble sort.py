#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swap=0
    for i in range (len(a)-1):
        for j in range(i, len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
                swap+=1
    print("Array is sorted in", swap, "swaps.")
    print("First Element:",a[0])
    print ("Last Element:",a[-1])
    return


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
