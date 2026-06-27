RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
common_password=("password","1234","user","000000","4321")

password=input("Enter a password: ")
if password.lower() in common_password:
    print(f"{RED}Your Password is very weak{RESET}")
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
        Missing_Feedback.append("Add lowercase letter (a-z)\n")
    if any(c in "!@#$%^&*" for c in password):
        score+=1
    else:
        Missing_Feedback.append("Add symbol like !@#$%^&*")
    
    if score==4:
        print(f"{GREEN}Security status: Strong\n {RESET}")
    elif score==3:
        print(f"{YELLOW}Security status: Medium\n {RESET}")
    elif score==2:
        print(f"{RED}Security status: Weak\n {RESET}")
    else:
        print(f"{RED}Security status: Very Weak\n {RESET}")

    if Missing_Feedback:
        print(f"{YELLOW}Suggestions to make it stronger: {RESET}")
        for task in Missing_Feedback:
            print(" ", task)
    else:
        print("No Missing_Feedback. Your password is already okay.")
print("-----------------------------------------------------------------------")
        
