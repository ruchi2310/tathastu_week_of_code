# tathastu_week_of_code
def findMissingNo(list,n):
    for i in range(n):
        if(list[i]<=0 or list[i]>n):
            continue
        val=list[i]
        while(list[val-1]!=val):
            nextval=list[val-1]
            list[val-1]=val
            val=nextval
            if(val<=0 or val>n):
                break
    for i in range(n):
        if(list[i]!=i+1):
            return i+1
        return n+1

if __name__=="__main__":
    list=[2,3,7,6,8,-1,-10,15]
    list_size=len(list)
    missing=findMissingNo(list,list_size)
    print("the smallest positive","missing number is",missing)
