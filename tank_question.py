h=int(input("enter the height:-"))
r=int(input("enter the radius:-"))
v=3.14*(r**2)*h
fr=15
t=int(input("enter the time:-"))
v_f=15*t
if  v==v_f:
    print("filled completely")
elif v_f<v:
    print("underflow")
else:
    print("overflow")