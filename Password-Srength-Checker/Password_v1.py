
password=input("Enter your password: ")
print("your password: ",password) 
common_passwords=(1234,123456,"password","user")

if any(c.isupper() for c in password)==False:
    print("create a password including capital letter for more secure")
elif any(c.islower() for c in password)==False:
    print("create a password including simple letter for more secure")
