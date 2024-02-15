#Calculator Program (CLI)


def calculator():
    
    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid number")    
        
    # try:
    #     num2 = int(input("Enter second number: "))
    # except ValueError:
    #     print("Invalid second number")
    #     num2 = int(input("Enter second number again: "))
    user_operation = input("Enter the operation you want to perform among + - * or / :")
    if(user_operation == "+"):
        d = num1 + num2
    elif(user_operation == "-"):
        d = num1 - num2    
    elif(user_operation == "*"):
        d = num1 * num2    
    elif(user_operation == "/"):
        d = num1 / num2
    else: 
        print("Invalid operation") 

    print("The result is ",d)  

calculator()

while True:
    try:
        user_choice = input("do you want to use the program again? (y/n)")
        if(user_choice =="y" or user_choice == "Y"):
            calculator()
        elif(user_choice =="n" or user_choice =="N"):
            print("Thankyou for using this program")
            break
    except:
        print("Invalid input")
    