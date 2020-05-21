# tathastu_week_of_code
N=int(input("enter the value of N"))
a=0
b=1
print("fibonacci series",N,"number are following")
for i in range(N):
    print(a,end=" ")
c=a+b
a=b
b=c
