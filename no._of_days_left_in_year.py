d=int(input("ENTER THE DATE:-"))
m=int(input("ENTER THE MONTH NO.:-"))
cd=d+((m-1)*30)
out=365-cd
print("remaining days in this year:-",out)