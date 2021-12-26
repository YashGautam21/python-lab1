x=list(map(int,input()))
c=0
s=0
while(s!=6174):
    a=sorted(x,reverse=True)
    b=sorted(x)
    a=[str(i) for i in a]
    b=[str(i) for i in b]
    a=''.join(a)
    b=''.join(b)
    s=int(a)-int(b)
    
    f=str(s)
    x=list(map(int,f))
    c+=1
print(c)    

