def div(y):
      a=y[0]
      b=y[1]
      c=0
      while(a>=b):
        a-=b
        c+=1
      return c    
ls=list(map(int,input().split()))
out=div(ls)
print(out)




