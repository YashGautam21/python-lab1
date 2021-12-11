def hcf(x,y):
    if x>y:
        s=y
    else:
        s=x
    for i in range(1,s+1):
         if x%i==0 and y%i==0:
             hcf=i
    return hcf    
def lcm():
    return (a*b//hcf(a,b))
a=int(input())     
b=int(input())    
print(hcf(a,b))
print(lcm())