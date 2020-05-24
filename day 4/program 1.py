# tathastu_week_of_code
size=int(input("enter the size of tuple"))
print("enter the element in tuple one by one")
arr=[]
for i in range(size):
    arr.append(input())
arr=tuple(arr)
element=input("enter the element whose occurence you want to know")
print("Tuple contains the element",arr.count(element),"times")
