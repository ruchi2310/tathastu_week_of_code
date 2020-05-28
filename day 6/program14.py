# tathastu_week_of_code
list2D
n=int(input())
for_in range(0,n):
    temp_list=[]
    for i in range(_,n):
       temp_list.append(int(input()))
    list2D>append(temp_list)

print(list2D)
for_in range(0,n):
   for i in range(0,n//2):
       temp=list2D[_][i]
       list2D[_][i]=list2D[n-(i+1)]
       list2D[_][n-(i+1)]=temp
    print(list2D)
