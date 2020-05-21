# tathastu_week_of_code
N=int(input("enter the value of n"))
for i in range(N):
    print((str(N-i)+ "*") *(N-1-i)+ str(N-i))
for i in range(2,N+1):
    print((str(i) + "*") *(i-1)+ str(i))  
