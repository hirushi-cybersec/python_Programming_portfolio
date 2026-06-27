
common_password=("password","1234","user","000000","4321")
password=input("Enter a password: ")c
if password.lower() in common_password:
    print("Your Password is very weak")
    print("Reason: This is very common_password")
else:
    score=0
    Missing_Feedback=[]

    if len(password)>=8:
        score+=1
    else:
        Missing_Feedback.append("create a password at least with 8 characters\n")
    
    if any(c.isupper()for c in password):
        score+=1
    else:
        Missing_Feedback.append("Add uppercase letter (A-Z)\n")
    if any(c.islower() for c in password):
        score+=1
    else:
        Missing_Feedback.append("Add lowercase letter (a-z)\nc")
    if any(c in "!@#$%^&*" for c in password):
        score+=1
    else:
        Missing_Feedback.append("Add symbol like !@#$%^&*")
    
    if score==4:
        print("Security status: Stong\n")
    elif score==3:
        print("Security status: Medium\n")
    elif score==2:
        print("Security status: Weak\n")
    else:
        print("Security status: Very Weak\n")

    if Missing_Feedback:
        print("Suggestions to make it stronger: ")
        for task in Missing_Feedback:
            print(" ", task)
    else:
        print("No Missing_Feedback. Your password is already okay.")
        
