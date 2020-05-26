# tathastu_week_of_code
def kthsmallest(list,n,k):

    list.sort()
    return list[k-1]
if __name__=='__main__':
     list=[12,3,4,7,9]
     n=len(list)
     print(list)
     k=2
     print("k'the smallest element is",kthsmallest(list,n,k))
