#Input Statement

# a = int(input("Enter any number"))
# print(a)

#Calculator Program (CLI)

while True:
    a = int(input("Enter your first number: "))
    b = int(input("Enter second number: "))
    c = input("Enter the operation you want to perform among + - * or / :")
    if(c == "+"):
        d = a + b
    elif(c == "-"):
        d = a - b    
    elif(c == "*"):
        d = a * b    
    elif(c == "/"):
        d = a / b
    else: 
        print("Invalid operation") 

    print("The result is ",d)   

    user_choice = input("do you want to use the program again? (y/n)")
    if(user_choice =="y" or user_choice == "Y"):
        continue
    elif(user_choice =="n" or user_choice =="N"):
        print("Thankyou for using this program")
        break
    else:
        print("Invalid answer")
        break