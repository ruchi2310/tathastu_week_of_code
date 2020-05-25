# tathastu_week_of_code
def house(List):
   if len(List)==2:
   return max(List)
   if len(List)==1:
   return List[0]
   if len(List)==3:
    return max(List[1],List[0]+house(List[2:]))
    return max(List[1]+house(List[3:]),List[0]+house(List[2:]))
    size=int(input("enter the number of houses in aline"))
    List=[]
    for i in range(size):
    List.append(int(input("enter the value in the house number"+str(i+1)+":")))
    print("the maximum stolen value from house is",house(List))
