# tathastu_week_of_code
ize=int(input("enter the no of items you want  to add dictonary"))
diction=dict()
for i in range(size):
    key=input("enter the key for item" + str(i+1) +" dictonary:")
    value=int(input("Enter the value for item" + str(i+1) + " in dictonary"))
    diction[key]=value
    print("the second largest value in the dictonary is",list(sorted(diction.values()))[-2])
