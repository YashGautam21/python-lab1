st=input().upper() 
for i in range(65,91):
    if chr(i) not in  st:
        break
    else:
        f=1
print('panagram' if f==1 else 'not')
    
    