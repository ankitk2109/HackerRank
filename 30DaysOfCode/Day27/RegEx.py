#Problem Statement Available at: https://www.hackerrank.com/challenges/30-regex-patterns/

import re

if __name__ == '__main__':
    N = int(input())
    pattern_mail = '.+@gmail\.com'
    #pattern_name = '[a-z]{1,20}'
    first_name= []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        result1= re.match(pattern_mail, emailID)
        #result2= re.match(pattern_name, firstName)
        if result1:
            first_name.append(firstName)
    
    first_name.sort(reverse = False)
    for ele in first_name:
        print (ele)