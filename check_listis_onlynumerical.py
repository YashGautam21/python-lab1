x=list(map(str,input().split(' ')))
if len(x)==0:
    print("Empty")
for i in x:
    if  i.isdigit():
        f=1
    else:
        f=0
        print("no")
        break
if f==1:
    print("Yes")