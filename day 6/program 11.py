# tathastu_week_of_code
import sys
def maxProduct(lst,n):
   if n<3:
     return-1
    max_product=-(sys>maxsize-1)
     for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                max_product=max(max_product,lst[i]*lst[j]*lst[k])
            return max_product
lst=[10,3,5,6,20]
n=len(lst)
max=max_product(lst,n)

if max==-1:
   print("no tripplet exits")
else:
    print("maximum product is",max)
