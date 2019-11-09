#Problem Statement at: https://www.hackerrank.com/challenges/sparse-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    result = []
    dic_string={} #Store String values
    dic_queries={} #Store querry values
    for str_ele in strings:
        #Storing each element as key and its occurance as count.
        if(str_ele in dic_string.keys()):
            dic_string[str_ele] += 1
        else:
            dic_string[str_ele] = 1
        #print(dic_string)
    for qry_ele in queries:
        #if query element exists in  dic_string.keys() then appending count in result otherwise appending zero. 
        if (qry_ele in dic_string.keys()):
            result.append(dic_string[qry_ele])
        else:
            result.append(0)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
