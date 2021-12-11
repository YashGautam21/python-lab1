x=list(map(int,input().split()))
ls=0
for i in x:
    ls=ls+i
print(ls)
if ls%2==0:
    print("True")
else:
    print("False")