n=int(input())
count=0
for i in range(2**n):
    if '11' in bin(i):        
        count+=1
print(count)