ls=list(map(int,input().split()))
ls1=[]
for i in range(1,ls[-1]+1):
    if  i not in ls:
        ls1.append(i)
print(ls1)