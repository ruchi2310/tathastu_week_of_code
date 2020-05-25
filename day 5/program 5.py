# tathastu_week_of_code
def sortEvenOdd(list):
odd=[]
even=[]
for x in list:
if x%2==0:
even.append(x)
else:
odd.append(x)
return sorted(odd,reverse=true)+sorted(even)
size=int(input("enter the no. of element you want  to add in the array:"))
list=[]
for i in range(size)
list.append(int(input("enter the element number"+str(i+1)+" in the list")))
print("the list of number after sorting them according to given condition is ",str(sortEvenOdd(list)))
