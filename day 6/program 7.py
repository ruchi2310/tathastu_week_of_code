# tathastu_week_of_code
ef a(m,n,s="% s"):
    print(s%("a(%d,%d)" %(m,n)))
    if m==0:
        return n+1
    if n==0:
        return a(m-1,1,s)
    n2=a(m,n-1,s%("a(%d,%%s)"%(m-1)))
    return a(m-1,n2,s)
print(a(1,2))
