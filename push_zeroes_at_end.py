ls=list(map(int, input().split()))
ls1=[]
l=len(ls)
c=0
for i in ls:
    if i!=0:
        ls1.append(i)
    else:
       c+=1
for j in range(1,c+1):
    ls1.append(0)
print(ls1)      