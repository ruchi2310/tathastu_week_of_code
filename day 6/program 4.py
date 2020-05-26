# tathastu_week_of_code
from itertools import permutations
number=input("enter the digit:=")
choices=list(map(int,number))
res2=[]
for i in res2:
    res2.append(int(''.join(i)))
res2=sorted(res2)
print(res2[res2.index(int(number))+1])
