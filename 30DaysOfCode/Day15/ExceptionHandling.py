#Problem Statement at: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/

#!/bin/python3

import sys


S = input().strip()

try:
    print(int(S))
except:
    print('Bad String')
