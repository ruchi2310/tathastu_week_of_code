# tathastu_week_of_code
import math
def checkperfectsquare(n):
    sqrt=int(math.sqrt(n))
    if pow(sqrt,2)==n:
        return True
    else:
        return False
    
def isfibonacciNumber(n):
    res1=5*n*n+4
    res2=5*n*n-4
    if checkperfectsquare(res1) or checkperfectsquare(res2):
        return True
    else:
       return False
num=int(input("enter the integer number"))
if isfibonacciNumber(num):
    print("yes.",num,"is a fibonacci number")
else:
    print("no,",num,"is not a fibonacci number")
