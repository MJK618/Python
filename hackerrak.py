#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    
    query_r=[0]*len(query)
    for i in range(len(dictionary)): 
        for j in range(len(query)):
            if dictionary[i] != query[j] and (sorted(dictionary[i])==sorted(query[j])):
                query_r[j] +=1  
            if dictionary[i] == query[j]:
                query_r[j] +=1        
    return query_r
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
