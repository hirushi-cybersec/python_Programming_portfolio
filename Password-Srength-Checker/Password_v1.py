
common_password=("password","1234","user","000000","4321")
password=input("Enter a password")
if password.lower() in common_password:
    print("Password is very weak")
    print("Reason: This is very common_password")
else:
    score==0

    if len(password)>=8:
        score+=1
    else:
        print("create a password at least with 8 characters")
    if any(c.isupper() in password:
        score+=1
    else:
        printf("Add uppercase letter (A-Z)")
    
