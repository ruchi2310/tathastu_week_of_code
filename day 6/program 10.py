# tathastu_week_of_code
lst=[]
n=int(input("enter number of list n"))
for i in range(0,n):
    print("list",i)
    k=int(input("enter the no.of element"))
    for j in range(0,k):
        ele=int(input())
        lst.append(ele)
    print(lst)
print("merge list is k=",lst)
