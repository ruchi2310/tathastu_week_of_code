# tathastu_week_of_code
def knapsack(weight,list):
   if weight==0:
   return 0
   if len(list)==1:
   if list[0][0]>weight:
   return 0
   return list[0][1]
   if list[0][0]>weight:
   retun knapsack((weight,list[1:]))
   return max(list[0][1]+knapsack(weight-list[0][0],list[1:]),knapsack(weight,list[1:]))
   size=int(input("enter the number of item you want to enter"))
   list=[]
   for i in range(Size)
     weight=int(input("Enter the weight for otem number"+str(i+1)+":"))
     value=int(input("enter the valuefor item number"+str(i+!)+":"))
     list.append((weight,value))
     weight=int(input("enter the value of weight capacity"))
     print("the maximum value for the given weight value pair is",knapsack(weight,list))
     
