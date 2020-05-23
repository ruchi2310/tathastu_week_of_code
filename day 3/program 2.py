# tathastu_week_of_code
def permutation(list,string=""):
    Set=set(list)
    stringList=[]
    if len(set)==1:
        string+= "".join(list)
        return list([string])
    for x in Set:
        List1=list(list)
        s=string+x
        List1.remove(x)
        stringList.extend(permutation(List1,s))
        return stringList

string=input("enter a string:")
list=permutation(list(string))
print("all permutation of given string is "+",".join(list))
