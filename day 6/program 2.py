# tathastu_week_of_code
def sortlist0and1(lst,n):
    count=0
    for i in range(0,n):
        if(lst[i]==0):
           count=count+1
    for i in range(0,count):
        lst[i]=0
    for i in range(count,n):
        lst[i]=1
def print_list(arr,n):
    print("list after sorted is",end="")
    for i in range(0,n):
        print(lst[i],end=" ")
lst=[0,1,0,1,1,1]
n=len(lst)
sortlist0and1(lst,n)
print_list(lst,n)
