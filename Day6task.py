#ask for the data and no. of times they want to print the data and print the data accordingly

user_data = input("Enter the data you want to print: ")
num = int(input(f"Enter the number of times you want to print the data, '{user_data}': "))
while num> 0:
    print(user_data)
    num -= 1 
    