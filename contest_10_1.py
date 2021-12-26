import collections
n=int(input())
x=list(map(str,input().split()))
x.sort()
ls=[]
ls1=[]
for i in x:
    ls.append(i[0])
    ls1.append(i[-1])
if collections.Counter(ls)==collections.Counter(ls1):
                     print(True)
else:
                     print(False)         
                     
                     
                              
                      
        