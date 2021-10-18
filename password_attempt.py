p=1234
i=3
while(i>=0):
	x=int(input("enter the password::"))
	if x==p:
		
		print("successfully login")
		break
	else:
		i=i-1
		print("login fail")
		print(f"{i}attempts left")
        
