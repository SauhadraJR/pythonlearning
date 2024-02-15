#Exception handling
try: 
    num1 = int(input("Enter a number : "))
    print(num1)
except ValueError:
    print("Not a valid number!")    
# try:
#     print(num1)
except NameError:
    print("Variable not initialized!")