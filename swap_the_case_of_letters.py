x=input()
st=''
for i in x:
    if ord(i)  in range(65,91):
        st+=chr(ord(i)+32)    
    else:
        if ord(i) in range(97,127):
             st+=chr(ord(i)-32)
print(st)            