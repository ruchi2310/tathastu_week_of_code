# tathastu_week_of_code
ze=int(input("enter the no of items you want  to add dictonary"))
diction=dict()
for i in range(size):
    key=input("enter the key for item" + str(i+1) +" dictonary:")
    value=int(input("Enter the value for item" + str(i+1) + " in dictonary"))
    diction[key]=value
    result=dict()
    for key,value in diction.items():
        if value not in result.values():
            result[key]=value
    print("dictonary after removing duplicate values:",result)
