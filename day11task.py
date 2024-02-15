a = {}
while True: 
    
    user_input = input("Do you have the account? [y/n]")
    if(user_input == "y" or user_input == 'Y'):
        user_name = input("Enter your username: ")
        user_password = input("Enter your password: ")
        if (user_name in a) and (a[user_name]==user_password):
            print("login successful!!")
        else:
            print("User not found!!")
    elif(user_input == "n" or user_input == 'N'):
        user_name = input("Enter username you want to create: ")
        user_password = input("Create a password: ")
        a[user_name] = user_password
    user_input2 = input("Do you want to continue? [y/n]")
    if(user_input2 == "y" or user_input2 == "Y"):
        continue
    elif(user_input2 == "n" or user_input2 == "N"):
        print("Thankyou")
        break
    else:
        print("Invalid input")
