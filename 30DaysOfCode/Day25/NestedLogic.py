#Problem Statement Available at: https://www.hackerrank.com/challenges/30-nested-logic

def cal_fine(act,exp):
    
    Ye, Ya, Me, Ma, De, Da = int(exp[2]), int(act[2]), int(exp[1]), int(act[1]), int(exp[0]), int(act[0])

    if(Ya < Ye):
        return 0
    elif(Ya == Ye):
        if(Ma < Me):
            return 0
        elif(Ma == Me):
            if(Da < De ):
                return 0
            elif(Da == De):
                return 0
            else:
                return (15 * (Da - De)) 
        else:
            return (500 * (Ma - Me))
    else:
        return (10000)


actual_date = input().split()
expected_date = input().split()

#Alternatively we can also take input as:
#d1, m1, y1 = map(int, input().split())
#d2, m2, y2 = map(int, input().split())

print(cal_fine(actual_date,expected_date))