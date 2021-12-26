x=input()
d=0
st=''
for i in x:
    if i.isalpha() or i.isdigit() or i=='_' or i=="/ ":
        st+=i
        c=True
    else:
        if c==True:
            st+='_'
            c=False
print(st)  