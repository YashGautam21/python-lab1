def fun1(a,t,p=[]):
    s=sum(p)
    if s==t:
        print(p)
    for i in range(len(a)):
        k=a[i]
        r=a[i+1:]
        fun1(r,t,p+[k])
x=list(map(int,input().split()))
n=int(input())
fun1(x,n)